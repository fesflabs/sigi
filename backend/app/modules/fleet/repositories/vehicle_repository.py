from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List, Optional
from ..models import Vehicle
from ..schemas import VehicleCreate

class VehicleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: VehicleCreate) -> Vehicle:
        vehicle = Vehicle(**data.model_dump())
        self.session.add(vehicle)
        await self.session.commit()
        await self.session.refresh(vehicle)
        return vehicle

    async def get_all(self) -> List[Vehicle]:
        result = await self.session.execute(select(Vehicle))
        return result.scalars().all()

    async def get_by_id(self, vehicle_id: int) -> Optional[Vehicle]:
        result = await self.session.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
        return result.scalars().first()
