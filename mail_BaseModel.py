from pydantic import BaseModel,EmailStr
from typing import Optional
from typing import List
from pydantic import Field


class DataEmail(BaseModel):
    id_email: int
    name_email: EmailStr
    


def create_data_picture_in_db(email_in_db):
    data = DataEmail(
                        id_email=email_in_db.id_email,
                        name_email = email_in_db.name_email)
    return data

class RequestDataEmail(BaseModel):
    name_email: EmailStr

class ResponceDataEmail(BaseModel):
    success: bool
    error: str | None
    data: DataEmail

