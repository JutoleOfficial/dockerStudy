from fastapi import FastAPI, Query
import socket
import os
import requests

app = FastAPI()

MY_NAME = os.getenv("MY_NAME", "unknown")


@app.get("/")
def runApp():
    return {"message": "HELLO-WORLD"}


@app.get("/my-ip")
def read_id():
    return {"ip": socket.gethostbyname(socket.gethostname())}


@app.get("/name")
def my_name():
    return {"name": MY_NAME}


@app.get("/send")
def send(ip: str = Query(regex=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")):
    res = requests.get(f"http://{ip}:9123/name")
    data = res.json()
    if res.status_code == 200:
        data.update({"result": "success"})
    else:
        data = {"result": "failed"}
    return data


@app.get("/send2")
def send2(name: str = Query()):
    res = requests.get(f"{name}:9123/name")
    if res.status_code == 200:
        data = res.json()
        data["result"] = "success"
    else:
        data["result"] = "failed"
    return data
