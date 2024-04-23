from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from doctor_model import Doctor
from patient_model import Patient

class Appointment(BaseModel):
    appointment_id:str
    doctor:Doctor
    patient:Patient
    appointment_date:Optional[datetime]