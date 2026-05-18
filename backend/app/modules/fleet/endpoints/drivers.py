from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_session
from app.core.auth import get_current_user, User
from ..schemas import DriverCreate, DriverResponse
from ..repositories.driver_repository import DriverRepository

router = APIRouter(prefix="/drivers", tags=["Fleet - Drivers"])

def require_gestor(user: User = Depends(get_current_user)):
    if user.role != "Gestor de Logistica":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Apenas Gestor de Logistica pode acessar.")
    return user

@router.post("", response_model=DriverResponse)
async def create_driver(
    data: DriverCreate,
    session: AsyncSession = Depends(get_session),
    user: User = Depends(require_gestor)
):
    repo = DriverRepository(session)
    return await repo.create(data)

@router.get("", response_model=List[DriverResponse])
async def list_drivers(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(require_gestor)
):
    repo = DriverRepository(session)
    return await repo.get_all()
