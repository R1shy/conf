from typing import Annotated

from asyncpg import Connection
from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

from models.event import Event, SimpleEvent
from services.event import EventService
from utils.db import use_db

router = APIRouter(tags=["Event"])


@router.get(
    "/event/{event_key}",
    operation_id="getByKey",
    responses={200: {"model": Event}},
)
async def get_by_key(
    event_key: str, db: Annotated[Connection, Depends(use_db)]
) -> Event:
    service = EventService(db)
    data = await service.get_by_key(event_key)

    if not data:
        raise HTTPException(status_code=404, detail="Event not found")

    return data


@router.get(
    "/team/{number}/events/{year}",
    operation_id="getByTeamAndYear",
    responses={200: {"model": Event}},
)
async def get_by_team_and_year(
    number: int, year: int, db: Annotated[Connection, Depends(use_db)]
) -> list[Event]:
    service = EventService(db)
    return await service.get_by_team_and_year(f"frc{number}", year)


@router.get(
    "/team/{number}/events/{year}/simple",
    operation_id="getByTeamAndYearSimple",
    responses={200: {"model": SimpleEvent}},
)
async def get_by_team_and_year_simple(
    number: int, year: int, db: Annotated[Connection, Depends(use_db)]
) -> list[SimpleEvent]:
    service = EventService(db)
    return await service.get_by_team_and_year_simple(f"frc{number}", year)
