from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from .models import ReservationStatus

class FleetBaseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

# Driver Schemas
class DriverCreate(FleetBaseSchema):
    name: str
    registration_number: str
    cost_center: str
    user_id: Optional[int] = None

class DriverResponse(DriverCreate):
    id: int

# Vehicle Schemas
class VehicleCreate(FleetBaseSchema):
    brand: str
    model_name: str
    manufacture_year: int
    model_year: int
    initial_mileage: int
    driver_id: Optional[int] = None

class VehicleResponse(VehicleCreate):
    id: int

# Reservation Schemas
class ReservationDestinationSchema(FleetBaseSchema):
    destination: str

class ReservationPassengerSchema(FleetBaseSchema):
    passenger_name: str

class ReservationCreate(FleetBaseSchema):
    start_datetime: datetime
    end_datetime: datetime
    origin: str
    destinations: List[ReservationDestinationSchema]
    activity: str
    passenger_count: int
    passengers: List[ReservationPassengerSchema]
    observation: Optional[str] = None

class ReservationResponse(ReservationCreate):
    id: int
    requester_id: int
    status: ReservationStatus
    vehicle_id: Optional[int] = None
    
# Dashboard Metrics
class DashboardMetricsResponse(FleetBaseSchema):
    total_reservations: int
    approved_reservations: int
    pending_reservations: int
    pending_next_24h: int
