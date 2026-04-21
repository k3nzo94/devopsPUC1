from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/hello")
async def read_root():
    return {"Hello": "World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "nun_aleatorio": random.randint(0, 1000)}

