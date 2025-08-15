from fastapi import FastAPI
from tugas1 import get_html,get_quotes

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/tugas1")
def get_quote():
    quotes = get_quotes()
    return {"quotes": quotes}