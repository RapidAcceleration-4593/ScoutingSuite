from fastapi import FastAPI
from pydantic import BaseModel
import logging

class Team(BaseModel):
    number: int
    name: str

app = FastAPI()
logger = logging.getLogger("uvicorn")

@app.get("/")
async def root():
    return { "message": "Hello World" }

@app.post("/items/")
async def recieveItem(team: Team):
    logger.info("Recieved a team of name " + team.name)