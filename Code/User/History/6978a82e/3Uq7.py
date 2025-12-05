from fastapi import APIRouter
from fastapi.requests import Request

router = APIRouter()

@router.post("/firehose")
async def firehose(req: Request):
    dat = await req.body()
    print(dat.decode())
    return 200 # 200 or prune
