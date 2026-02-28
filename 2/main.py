from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# для принятия данных
class Numbers(BaseModel):
    num1: float
    num2: float

# отдаем статические файлы (html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# api endpoint
@app.post("/calculate")
def calculate(data: Numbers):
    result = data.num1 + data.num2
    return {"result": result}