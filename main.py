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

app = FastAPI()


@app.get("/")
def response_html():
    return FileResponse("adminka.html")


@app.post("/add_email")
def add_email(req:RequestDataEmail):
    print("add_email")
    return ResponceDataEmail(success = True)
    # with Session() as session:
    #     check_email = session.query(EmailList).filter(EmailList.name_email == req.name_email).first()
    #     if check_email:
    #         return JSONResponse(
    #         status_code=status.HTTP_400_BAD_REQUEST, 
    #         content={"error": "Такой Email уже существует!"})
        
    #     create_email = EmailList()
    #     create_email.name_email = req.name_email

    #     session.add(create_email)
    #     session.commit()

    #     return ResponceDataEmail(success = True,error="", data = create_data_email_in_db(create_email))

