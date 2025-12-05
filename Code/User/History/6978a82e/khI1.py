from ast import literal_eval

from fastapi import APIRouter
from fastapi.requests import Request

import main
from utils.logging import LogLevel

router = APIRouter()


@router.post("/firehose")
async def firehose(req: Request) -> int:
    dat = await req.body()
    data = literal_eval(dat.decode("utf-8"))
    
    return 200  # 200 or prune
