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
def add_email(req:RequestDataEmail[Query(max_length=50)]):
    with Session() as session:
        pass

