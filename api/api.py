from fastapi import FastAPI

app = FastAPI()

@app.get("/helloWorld")
def helloWorld():
    return {"Hello": "World"}