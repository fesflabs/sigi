from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List, Optional
from ..models import Driver
from ..schemas import DriverCreate

class DriverRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: DriverCreate) -> Driver:
        driver = Driver(**data.model_dump())
        self.session.add(driver)
        await self.session.commit()
        await self.session.refresh(driver)
        return driver

    async def get_all(self) -> List[Driver]:
        result = await self.session.execute(select(Driver))
        return result.scalars().all()

    async def get_by_id(self, driver_id: int) -> Optional[Driver]:
        result = await self.session.execute(select(Driver).where(Driver.id == driver_id))
        return result.scalars().first()
