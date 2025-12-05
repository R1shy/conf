from __future__ import annotations
from fastapi import APIRouter
from fastapi.requests import Request
from pydantic import BaseModel

router = APIRouter()

@router.post("/firehose")
async def firehose(req: Request):
    dat = await req.body()
    print(dat.decode())
    return 200 # 200 or prune
