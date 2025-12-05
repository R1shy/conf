# NOT THE SCOUTING SCHEMA, see match_scouting.py for that
# this is the analysis schema of matches

from typing import TypedDict

from pydantic import BaseModel


# Subject to change
class MatchBreakdown(TypedDict):
    score: int
    no_foul_points: int | None
    foul_points: int | None
    auto_points: int | None
    teleop_points: int | None
    endgame_points: int | None
    endgame_1: int | None
    endgame_2: int | None
    endgame_3: int | None
    rp_1: bool | None
    rp_2: bool | None
    rp_3: bool | None
    comp_1: int | None
    comp_2: int | None
    comp_3: int | None
    comp_4: int | None
    comp_5: int | None
    comp_6: int | None
    comp_7: int | None
    comp_8: int | None
    comp_9: int | None
    comp_10: int | None
    comp_11: int | None
    comp_12: int | None
    comp_13: int | None
    comp_14: int | None
    comp_15: int | None
    comp_16: int | None
    comp_17: int | None
    comp_18: int | None


class MatchAlliance(TypedDict):
    teams: list[str]
    dq: list[str]
    backups: list[str]


# TODO: Add model validation
# TODO: deal with breakdowns
class Match(BaseModel):
    key: str
    event_key: str
    match_type: str  # type is a keyword
    match_num: int
    set_num: int
    red_score: int
    blue_score: int
    completed: bool
    winner: str
    time: int  # I <3 unix
    predicted_time: int  # I <3 unix
    video: str
    red_breakdown: MatchBreakdown
    blue_breakdown: MatchBreakdown

class SimpleMatch(BaseModel, frozen=True):
    key: str
    match_num: int
    type: str
    red_score: int | None = None
    blue_score: int | None = None
    completed: bool
    predicted_time: datetime
    winner: str | None = None
    video: str | None = None
    red_alliance: list[str]
    blue_alliance: list[str]
