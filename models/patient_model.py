from pydantic import BaseModel
from typing import List

from .user_model import User
from appointment_model import Appointment


class Patient(BaseModel):
    user:User
    weight:int
    height:int
    appointments:List[Appointment] = []

