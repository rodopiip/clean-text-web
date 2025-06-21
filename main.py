from operator import index
from typing import Annotated

from fastapi import FastAPI, Body
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from pydantic import BaseModel

class APITransferableText(BaseModel):
    text: str

# "{"text": "alabala"}"
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/clean")
async def clean_text(inbound_text: Annotated[APITransferableText, Body()]):
    return {"clean_text": inbound_text.text}
