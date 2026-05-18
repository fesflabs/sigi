from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from typing import List, Optional
from datetime import datetime, timedelta
from ..models import Reservation, ReservationDestination, ReservationPassenger, ReservationStatus
from ..schemas import ReservationCreate

class ReservationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, requester_id: int, data: ReservationCreate) -> Reservation:
        reservation_data = data.model_dump(exclude={"destinations", "passengers"})
        reservation = Reservation(requester_id=requester_id, **reservation_data)
        
        self.session.add(reservation)
        await self.session.flush() # Para pegar o ID da reservation
        
        for dest in data.destinations:
            rd = ReservationDestination(reservation_id=reservation.id, destination=dest.destination)
            self.session.add(rd)
            
        for passg in data.passengers:
            rp = ReservationPassenger(reservation_id=reservation.id, passenger_name=passg.passenger_name)
            self.session.add(rp)
            
        await self.session.commit()
        return await self.get_by_id(reservation.id)

    async def get_by_id(self, reservation_id: int) -> Optional[Reservation]:
        stmt = select(Reservation).where(Reservation.id == reservation_id).options(
            selectinload(Reservation.destinations),
            selectinload(Reservation.passengers)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def list_by_requester(self, requester_id: int) -> List[Reservation]:
        stmt = select(Reservation).where(Reservation.requester_id == requester_id).options(
            selectinload(Reservation.destinations),
            selectinload(Reservation.passengers)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_all(self) -> List[Reservation]:
        stmt = select(Reservation).options(
            selectinload(Reservation.destinations),
            selectinload(Reservation.passengers)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
        
    async def get_metrics(self) -> dict:
        # Dashboard metrics
        total = await self.session.execute(select(Reservation))
        total = len(total.scalars().all())
        
        approved = await self.session.execute(select(Reservation).where(Reservation.status == ReservationStatus.APPROVED))
        approved = len(approved.scalars().all())
        
        pending = await self.session.execute(select(Reservation).where(Reservation.status == ReservationStatus.PENDING))
        pending_list = pending.scalars().all()
        
        # Pending next 24h
        now = datetime.now()
        next_24h = now + timedelta(hours=24)
        pending_24h = sum(1 for p in pending_list if now <= p.start_datetime <= next_24h)
        
        return {
            "total_reservations": total,
            "approved_reservations": approved,
            "pending_reservations": len(pending_list),
            "pending_next_24h": pending_24h
        }
