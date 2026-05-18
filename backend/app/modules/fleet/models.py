from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class ReservationStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"

class Driver(SQLModel, table=True):
    __tablename__ = "fleet_driver"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    registration_number: str = Field(unique=True, index=True)
    cost_center: str
    user_id: Optional[int] = Field(default=None, description="Vinculo com usuário logado (motorista)")
    
    vehicles: List["Vehicle"] = Relationship(back_populates="driver")

class Vehicle(SQLModel, table=True):
    __tablename__ = "fleet_vehicle"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    brand: str
    model_name: str
    manufacture_year: int
    model_year: int
    initial_mileage: int
    
    driver_id: Optional[int] = Field(default=None, foreign_key="fleet_driver.id")
    driver: Optional[Driver] = Relationship(back_populates="vehicles")
    
    reservations: List["Reservation"] = Relationship(back_populates="vehicle")

class Reservation(SQLModel, table=True):
    __tablename__ = "fleet_reservation"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    requester_id: int = Field(index=True)
    start_datetime: datetime
    end_datetime: datetime
    origin: str
    activity: str
    passenger_count: int
    observation: Optional[str] = None
    status: ReservationStatus = Field(default=ReservationStatus.PENDING)
    
    vehicle_id: Optional[int] = Field(default=None, foreign_key="fleet_vehicle.id")
    vehicle: Optional[Vehicle] = Relationship(back_populates="reservations")
    
    destinations: List["ReservationDestination"] = Relationship(back_populates="reservation")
    passengers: List["ReservationPassenger"] = Relationship(back_populates="reservation")

class ReservationDestination(SQLModel, table=True):
    __tablename__ = "fleet_reservation_destination"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    reservation_id: int = Field(foreign_key="fleet_reservation.id")
    destination: str
    
    reservation: Optional[Reservation] = Relationship(back_populates="destinations")

class ReservationPassenger(SQLModel, table=True):
    __tablename__ = "fleet_reservation_passenger"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    reservation_id: int = Field(foreign_key="fleet_reservation.id")
    passenger_name: str
    
    reservation: Optional[Reservation] = Relationship(back_populates="passengers")
