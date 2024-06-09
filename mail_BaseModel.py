from pydantic import BaseModel
from typing import Optional
from typing import List
from pydantic import Field
from main import*


class DataEmail(BaseModel):
    id_email: int
    name_email: str


def create_data_picture_in_db(email_in_db):
    data = DataEmail(
                        id_email=email_in_db.id_email,
                        name_email = email_in_db.name_email)
    return data

class RequestDataEmail(BaseModel):
    name_email: str

class ResponceDataEmail(BaseModel):
    success: bool
    error: str | None
    data: DataEmail

