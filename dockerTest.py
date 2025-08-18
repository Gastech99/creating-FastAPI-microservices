from fastapi import FastAPI

app = FastAPI()

# Define a path operation decorator and function


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}