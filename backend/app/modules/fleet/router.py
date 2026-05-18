from fastapi import APIRouter
from .endpoints import drivers, vehicles, reservations

fleet_router = APIRouter(prefix="/fleet")

fleet_router.include_router(drivers.router)
fleet_router.include_router(vehicles.router)
fleet_router.include_router(reservations.router)
