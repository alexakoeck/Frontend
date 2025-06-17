import uvicorn
from fastapi import FastAPI
import requests

# change this to the address of the api server
API_SERVER_ADDRESS = "35.91.79.183"

app = FastAPI()

@app.get("/test")
def read_root():
    return {"message": "Hello World"}

@app.get("/")
def read_api(data: str | None = None):
    response = requests.post(f"http://{API_SERVER_ADDRESS}:8080/", params={"data": data})
    return f"summary: {response}"
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
