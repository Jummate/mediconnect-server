from pydantic import BaseModel, Field
from typing import List

from .user_model import User
from .appointment_model import Appointment


class Doctor(BaseModel):
    user:User
    specialty:str
    is_available : bool = Field(default=True)
    curr_appointment:Appointment
    appointments:List[Appointment] = []