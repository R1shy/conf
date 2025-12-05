from typing import Annotated

from asyncpg import Connection
from fastapi import APIRouter, Depends

from models.matches import Match
from services.match import MatchService
from utils.db import use_db

router = APIRouter(tags=["Match"])


@router.get(
    "/team/{number}/event/{event_key}/matches",
    operation_id="getByTeamAndEvent",
    responses={200: {"model": Match}},
)
async def get_by_team_and_event(
    number: int, event_key: str, db: Annotated[Connection, Depends(use_db)]
) -> list[Match]:
    service = MatchService(db)
    return await service.get_by_team_and_event(
        f"frc{number}", event_key
    )  # TODO: Verify query


@router.get(
    "/team/{number}/matches/{year}",
    operation_id="getMatchesByYear",
    responses={200: {"model": Match}},
)
async def get_by_team_and_year(
    number: int, year: int, db: Annotated[Connection, Depends(use_db)]
) -> list[Match]:
    service = MatchService(db)
    return await service.get_by_team_and_year(
        f"frc{number}", year
    )  # TODO: Verify query
