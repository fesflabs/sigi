from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_session
from app.core.auth import get_current_user, User
from ..schemas import VehicleCreate, VehicleResponse
from ..repositories.vehicle_repository import VehicleRepository

router = APIRouter(prefix="/vehicles", tags=["Fleet - Vehicles"])

def require_gestor(user: User = Depends(get_current_user)):
    if user.role != "Gestor de Logistica":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Apenas Gestor de Logistica pode acessar.")
    return user

@router.post("", response_model=VehicleResponse)
async def create_vehicle(
    data: VehicleCreate,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(require_gestor)
):
    repo = VehicleRepository(session)
    return await repo.create(data)

@router.get("", response_model=List[VehicleResponse])
async def list_vehicles(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(require_gestor)
):
    repo = VehicleRepository(session)
    return await repo.get_all()
