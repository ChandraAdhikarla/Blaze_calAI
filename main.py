from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Blaze_calAI"}

@app.get("/calculator", response_class=HTMLResponse)
async def calculator(request: Request):
    return "<html><body><h1>Calculator</h1><form action="/calculate" method="post">
        <input type="text" id="num1" name="num1"><br>
        <input type="text" id="op" name="op"><br>
        <input type="text" id="num2" name="num2"><br>
        <button type="submit">Calculate</button>
    </form></body></html>"

@app.post("/calculate")
async def calculate(num1: int, op: str, num2: int):
    if op == "+":
        return {"result": num1 + num2}
    elif op == "-":
        return {"result": num1 - num2}
    elif op == "*":
        return {"result": num1 * num2}
    elif op == "/":
        return {"result": num1 / num2}
    else:
        return {"error": "Invalid operation"}
