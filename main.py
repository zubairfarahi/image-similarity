from routes import route
from app import CONFIG

from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="odapi-compare",
    description="testing for image similiraty",
    contact={
        "name": "zubair",
        "email": "farahi.zubair121@gmail.com"
    }
    
)


app.include_router(route)
if __name__ == '__main__':
    uvicorn.run(app, host=CONFIG.host, port=int(CONFIG.port))
