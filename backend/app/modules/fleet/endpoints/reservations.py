from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_session
from app.core.auth import get_current_user, User
from ..schemas import ReservationCreate, ReservationResponse, DashboardMetricsResponse
from ..services.fleet_service import FleetService
from ..repositories.reservation_repository import ReservationRepository
from ..tasks import send_reservation_notification

router = APIRouter(prefix="/reservations", tags=["Fleet - Reservations"])

def require_fesf(user: User = Depends(get_current_user)):
    if user.role not in ["Trabalhador FESF", "Gestor de Logistica"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Sem permissão.")
    return user

@router.post("", response_model=ReservationResponse)
async def create_reservation(
    data: ReservationCreate,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(require_fesf)
):
    service = FleetService(session)
    reservation = await service.create_reservation(requester_id=user.id, data=data)
    # Schedule task sample
    send_reservation_notification.delay(reservation.id, "NOVA_RESERVA")
    return reservation

@router.get("", response_model=List[ReservationResponse])
async def list_reservations(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    repo = ReservationRepository(session)
    if user.role == "Trabalhador FESF":
        return await repo.list_by_requester(user.id)
    # Motorista ou Gestor podem ver mais, para simplificar:
    return await repo.get_all()

@router.get("/metrics", response_model=DashboardMetricsResponse)
async def get_metrics(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(get_current_user)
):
    if user.role != "Gestor de Logistica":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Apenas Gestor.")
    repo = ReservationRepository(session)
    return await repo.get_metrics()
