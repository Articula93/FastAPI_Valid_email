from fastapi import HTTPException
from pydantic import BaseModel,EmailStr, field_validator, model_validator
from typing import Optional
from typing import List
from pydantic import Field
from pydantic_core import PydanticCustomError


class RequestDataEmail(BaseModel):
    email: EmailStr

    @field_validator("email")
    def min_len_email(cls, value):
        print("field_validator name_email")
        if len(value) < 6:
            raise HTTPException(status_code=422, detail="email is to short")
        if len(value.split('.')[-1])<2:
            raise HTTPException(status_code=422, detail="domen is to short")
        return value

class ResponceDataEmail(BaseModel):
    success: bool
    error: str | None = None
    

class ResponseValidEmail(BaseModel):
    success: bool
    error: str | None = None
    
