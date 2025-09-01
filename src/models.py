from dataclasses import dataclass
from datetime import datetime

@dataclass
class Driver:
    id: str
    name: str
    license_number: str
    vehicle_info: dict
    current_location: tuple
    is_available: bool = True

@dataclass
class Passenger:
    id: str
    name: str
    phone: str
    rating: float = 5.0

@dataclass
class Ride:
    id: str
    driver_id: str
    passenger_id: str
    pickup_location: tuple
    destination: tuple
    status: str
    created_at: datetime


