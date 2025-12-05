from asyncpg import Connection

from models.event import Event, SimpleEvent


class EventService:
    def __init__(self, db: Connection) -> None:
        self.db = db

    async def get_by_key(self, event_key: str) -> Event | None:
        query = """
        SELECT events.key, events.name, events.event_type, events.week, events.year, events.start_date, events.end_date, events.district, events.city, events.state_prov, events.country
        FROM events
        WHERE events.key = $1;
        """
        records = await self.db.fetchrow(query, event_key)

        if not records:
            return

        return Event(**dict(records))

    async def get_keys_by_year(self, year: int) -> list[str]:
        query = """
        SELECT events.key
        FROM events
        WHERE events.year = $1;
        """
        records = await self.db.fetch(query, year)

        return [row["key"] for row in records]

    async def get_by_team_and_year(self, team_key: str, year: int) -> list[Event]:
        query = """
        SELECT events.key, events.name, events.event_type, events.week, events.year, events.start_date, events.end_date, events.district, events.city, events.state_prov, events.country
        FROM events
        JOIN team_events ON events.key = team_events.event_key
        WHERE team_events.team_key = $1 AND team_events.year = $2;
        """
        records = await self.db.fetch(query, team_key, year)
        return [Event(**dict(row)) for row in records]

    async def get_by_team_and_year_simple(
        self, team_key: str, year: int
    ) -> list[SimpleEvent]:
        query = """
        SELECT events.key, events.name, events.start_date
        FROM events
        JOIN team_events ON events.key = team_events.event_key
        WHERE team_events.team_key = $1 AND team_events.year = $2;
        """
        records = await self.db.fetch(query, team_key, year)
        return [SimpleEvent(**dict(row)) for row in records]
