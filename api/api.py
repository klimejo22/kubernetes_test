from fastapi import FastAPI, Request
import redis

redis_client = redis.Redis(host="redis", port=6379, db=0)
app = FastAPI()

@app.middleware("http")
async def count_requests(
    request: Request,
    call_next
):
    response = await call_next(request) 
    if response.status_code < 500:
        redis_client.incr("totalRequests")

    return response
    
@app.get("/helloWorld")
def helloWorld():
    return {"Hello": "World"}

@app.get("/stats")
def stats():
    return {"Total requests": redis_client.get("totalRequests")}

@app.get("/testNaHPA")
def test():
    a = 1
    while True:
        a = a * a + a
        print(a)