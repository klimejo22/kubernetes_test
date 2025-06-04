from fastapi import FastAPI, Request
import redis

redis_client = redis.Redis(host="redis", port=6379, db=0)
app = FastAPI()

@app.middleware("http")
async def count_requests(
    request: Request,
    call_next
):
    redis_client.incr("totalRequests")
    response = await call_next(request)
    return response
    
@app.get("/helloWorld")
def helloWorld():
    return {"Hello": "World"}

@app.get("/stats")
def stats():
    return {"Total requests": redis_client.get("totalRequests")}