import time
from datetime import datetime
from fastapi import APIRouter, Form, HTTPException, UploadFile
from fastapi.responses import UJSONResponse

route = APIRouter()



@route.get('/ping')
async def ping():
    
    time_n = datetime.fromtimestamp(time.time())
    time_now = time_n.strftime("%Y-%m-%dT%H:%M:%S+02:00")
    
    server_info = {
        "message": "ping test",
        "applicationName": "odapi-compare",
        "version": "v1.0.0",
        "serverTime": time_now
    }
    
    return server_info


@route.post('/similarity', response_class=UJSONResponse)
async def similarity(file1: UploadFile = Form(), file2: UploadFile = Form()):
    
    response = {}
    
    return response
    