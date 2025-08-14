from fastapi import FastAPI

app = FastAPI()

# Define a path operation decorator and function


@app.get("/")
async def root():
    return {"message": "Hello Word!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="172.0.0.1", port=8200)
