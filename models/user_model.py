from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    user_id:str
    first_name:str
    last_name:str
    age:int
    email:EmailStr
    gender:str
    phone:str
    created_at: datetime = datetime.now()

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"
   