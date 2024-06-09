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
# def add_email(req:RequestDataEmail[Query(min_length=10,max_length=50)]):

@app.get("/")
def response_html():
    return FileResponse("adminka.html")


@app.post("/add_email")
def add_email(req:RequestDataEmail):
    with Session() as session:
        create_email = EmailList()
        create_email.name_email = req.name_email

        session.add(create_email)
        session.commit()

    return ResponceDataEmail(success = True,error="", data = create_data_picture_in_db(create_email))

