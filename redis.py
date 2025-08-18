from fastapi import FastAPI
import redis


# Connect to redis service {hostname is 'redis' because of Docker Compose networking}
r = redis.Redis(host='redis', port=6379)

app = FastAPI

@app.get("/")
def read_root():
    # Chek Redis connection by incrementing a counter
    count = r.incr("hits")
    return {"message": "Hello, FastAPI with Redis", "Visit_count": count}