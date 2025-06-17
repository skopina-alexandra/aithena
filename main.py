from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello_world():
    return {
        "message": "Hello World"
    }


@app.get("/ola")
def ola():
    return {
        "message": "ola"
    }

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)