from datetime import datetime
from typing import Any

from asyncpg import Connection, PostgresError

from core import AppCore
from models.matches import Match
from services.event import EventService
from tba.client import TBAClient
from tba.utils import validate_year


class TBABoostrapService:
    def __init__(self, app: AppCore, *, db: Connection) -> None:
        self.db = db
        self.client = TBAClient(app)

    def __ensure_unix(self, m: Any) -> Match:  # noqa: ANN401
        return Match(
            key=m.key,
            event_key=m.event_key,
            match_type=m.type_of_match,
            match_num=m.match_num,
            set_num=m.set_num,
            red_score=m.red_score,
            blue_score=m.blue_score,
            completed=m.completed,
            winner=m.winner,
            time=m.time,
            predicted_time=int(m.predicted_time.timestamp())
            if isinstance(m.predicted_time, datetime)
            else m.predicted_time,
            video=m.video,
        )

    async def fetch_teams(self) -> int:
        query = """
                INSERT INTO teams (key, number, name, rookie_year, district, city, state_prov, country)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
                ON CONFLICT (key)
                DO UPDATE SET
                    number = EXCLUDED.number,
                    name = EXCLUDED.name,
                    rookie_year = EXCLUDED.rookie_year,
                    district = EXCLUDED.district,
                    city = EXCLUDED.city,
                    state_prov = EXCLUDED.state_prov,
                    country = EXCLUDED.country;
            """

        teams = await self.client.fetch_teams()

        try:
            async with self.db.transaction():
                await self.db.executemany(query, teams)
        except PostgresError as e:
            print(f"Database Insertion Error: {e}")
            raise

        return len(teams)

    async def fetch_events(self, year: int) -> int:
        query = """
        INSERT INTO events (key, name, event_type, week, year, start_date, end_date, district, city, state_prov, country)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        ON CONFLICT (key)
        DO UPDATE SET
            name = EXCLUDED.name,
            event_type = EXCLUDED.event_type,
            week = EXCLUDED.week,
            year = EXCLUDED.year,
            start_date = EXCLUDED.start_date,
            end_date = EXCLUDED.end_date,
            district = EXCLUDED.district,
            city = EXCLUDED.city,
            state_prov = EXCLUDED.state_prov,
            country = EXCLUDED.country
        """

        validate_year(year)  # TODO: implement error handling if this fails

        events = await self.client.fetch_events(year)

        try:
            async with self.db.transaction():
                await self.db.executemany(query, events)
        except PostgresError as e:
            print(f"Database Insertion Error: {e} ")
            raise

        return len(events)

    async def fetch_matches(self, year: int) -> int:
        match_query = """
        INSERT INTO matches (key, event_key, type_of_match, match_num, set_num, red_score, blue_score, completed, winner, time, predicted_time, video)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
        ON CONFLICT (key)
        DO UPDATE SET
            key = EXCLUDED.key,
            event_key = EXCLUDED.event_key,
            type_of_match = EXCLUDED.type_of_match,
            match_num = EXCLUDED.match_num,
            set_num = EXCLUDED.set_num,
            red_score = EXCLUDED.red_score,
            blue_score = EXCLUDED.blue_score,
            completed = EXCLUDED.completed,
            winner = EXCLUDED.winner,
            time = EXCLUDED.time,
            predicted_time = EXCLUDED.predicted_time,
            video = EXCLUDED.video
        """

        alliance_query = """
        INSERT INTO match_alliances (match_key, team_key, alliance, position, year)
        VALUES ($1, $2, $3, $4, $5)
        ON CONFLICT (match_key, alliance, position)
        DO UPDATE SET
            match_key = EXCLUDED.match_key,
            team_key = EXCLUDED.team_key,
            alliance = EXCLUDED.alliance,
            position = EXCLUDED.position,
            year = EXCLUDED.year
        """

        validate_year(year)  # TODO: implement error handling if this fails

        event_keys = await EventService(self.db).get_keys_by_year(2025)

        matches, alliances = await self.client.fetch_matches(event_keys)

        try:
            async with self.db.transaction():
                await self.db.executemany(
                    match_query,
                    [
                        tuple(self.__ensure_unix(m).model_dump().values())
                        for m in matches
                    ],
                )
                await self.db.executemany(alliance_query, alliances)
        except PostgresError as e:
            print(f"Database Insertion Error: {e} ")
            raise

        return len(matches)

    async def fetch_team_events(self, year: int) -> int:
        query = """
        INSERT INTO team_events (team_key, event_key, year)
        VALUES ($1, $2, $3)
        """
        validate_year(year)  # TODO: implement error handling if this fails

        event_keys = await EventService(self.db).get_keys_by_year(year)

        events = await self.client.fetch_team_events(event_keys, year)

        await self.db.executemany(query, events)

        return len(events)
