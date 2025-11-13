# 起動 uvicorn pyファイル名:FastAPI変数名 --reload
# uvicorn cord01_RestAPI_demo:app --reload

# pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

# 取得(GET)


@app.get("/hello")
def read_hello():
    return {"message": "Hello REST!"}

# 作成(POST)


@app.post("/items")
def create_item(item: dict):
    return {"received": item}
