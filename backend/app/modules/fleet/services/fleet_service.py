from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.reservation_repository import ReservationRepository
from ..schemas import ReservationCreate
from ..models import Reservation

class ReservationStrategy:
    def validate(self, data: ReservationCreate):
        raise NotImplementedError

class AdvanceTimeStrategy(ReservationStrategy):
    def __init__(self, min_hours: int = 12):
        self.min_hours = min_hours
        
    def validate(self, data: ReservationCreate):
        now = datetime.now()
        diff = data.start_datetime - now
        if diff < timedelta(hours=self.min_hours):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"A reserva deve ser feita com pelo menos {self.min_hours} horas de antecedência."
            )

class FleetService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.reservation_repo = ReservationRepository(session)
        self.strategies = [AdvanceTimeStrategy(min_hours=12)]

    async def create_reservation(self, requester_id: int, data: ReservationCreate) -> Reservation:
        # Validate strategies
        for strategy in self.strategies:
            strategy.validate(data)
            
        # Create reservation
        reservation = await self.reservation_repo.create(requester_id, data)
        return reservation
