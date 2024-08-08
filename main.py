from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Body, status, Response, Query
from typing import Annotated
from fastapi import Form
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse, FileResponse
from mail_db import*
from mail_BaseModel import*
import random
import base64
from datetime import datetime
from send_email import*
import uvicorn

app = FastAPI()


@app.get("/")
def response_html():
    return FileResponse("adminka.html")


@app.post("/add_email")
def add_email(req:RequestDataEmail):
    with Session() as session:
        check_email = session.query(EmailList).filter(EmailList.email == req.email).first()
        if check_email:
            return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={"error": "Такой Email уже существует!"})
        
        generate_name_valid = base64.urlsafe_b64encode(random.randbytes(30))

        if session.query(EmailList).filter(EmailList.check_valid == generate_name_valid).first():
            return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={"error": "Такая последовательность уже существует!"})
        
        current_datetime = datetime.now()

        create_email = EmailList()
        create_email.email = req.email
        create_email.check_valid = generate_name_valid
        create_email.is_valid = 0
        create_email.datetime = current_datetime

        session.add(create_email)
        session.commit()

        res = send_email(to_email = create_email.email,message = create_email.check_valid)

        if res == True:
            create_email.email_sent = 1
        else:
            create_email.email_sent = 0

        session.commit()

        return ResponceDataEmail(success = True,error="")

@app.get("/valid_email")
def valid_email(valid:str):
    with Session() as session:
        succession_from_email = session.query(EmailList).filter(EmailList.check_valid == valid).first()
        if succession_from_email:
            succession_from_email.is_valid = 1
        else:
            return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, 
            content={"error": "Нет такой последовательности!"})
        
        session.commit()

        return ResponseValidEmail(success = True,error="")
    

if __name__ == "__main__":
    uvicorn.run("main:app",host='195.133.144.169', reload=True)