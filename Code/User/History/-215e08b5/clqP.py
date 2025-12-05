from asyncpg import Connection

from models.matches import Match, SimpleMatch


class MatchService:
    def __init__(self, db: Connection) -> None:
        self.db = db

    async def get_by_team_and_event(self, team_key: str, event_key: str) -> list[Match]:
        query = """
        SELECT
            matches.key,
            matches.event_key,
            matches.type_of_match,
            matches.match_num,
            matches.set_num,
            matches.red_score,
            matches.blue_score,
            matches.completed,
            matches.winner,
            matches.time,
            matches.predicted_time,
            matches.video,
            ARRAY_AGG(
                match_alliances.team_key
                ORDER BY match_alliances.position
            ) FILTER (WHERE match_alliances.alliance = 'red') AS red_alliance,
            ARRAY_AGG(
                match_alliances.team_key
                ORDER BY match_alliances.position
            ) FILTER (WHERE match_alliances.alliance = 'blue') AS blue_alliance
        FROM matches
             JOIN
            match_alliances
            ON matches.key = match_alliances.match_key
        WHERE
            matches.key IN (
                SELECT match_key
                FROM match_alliances
                WHERE team_key = $1
            )
            AND matches.event_key = $2
        GROUP BY
            matches.key
        ORDER BY
            matches.match_num;
        """
        records = await self.db.fetch(query, team_key, event_key)
        return [Match(**dict(row)) for row in records]

    async def get_by_team_and_event_simple(self, team_key: str, event_key: str) -> list[SimpleMatch]:
        query = """
        SELECT
            matches.key,
            matches.match_num,
            matches.match_type,
            matches.red_score,
            matches.blue_score,
            matches.completed,
            matches.predicted_time,
            matches.winner,
            matches.video,
            ARRAY_AGG(
                match_alliances.team_key
                ORDER BY match_alliances.position
            ) FILTER (WHERE match_alliances.alliance = 'red') AS red_alliance,
            ARRAY_AGG(
                match_alliances.team_key
                ORDER BY match_alliances.position
            ) FILTER (WHERE match_alliances.alliance = 'blue') AS blue_alliance
        FROM matches
        JOIN
            match_alliances
            ON matches.key = match_alliances.match_key
        WHERE
            matches.key IN (
                SELECT match_key
                FROM match_alliances
                WHERE team_key = $1
            )
            AND matches.event_key = $2
        GROUP BY
            matches.key
        ORDER BY
            CASE matches.type
                WHEN 'em' THEN 1
                WHEN 'qm' THEN 2
                WHEN 'qf' THEN 3
                WHEN 'sf' THEN 4
                WHEN 'f' THEN 5
                ELSE 99
            END,
            matches.match_num;
        """
        records = await self.db.fetch(query, team_key, event_key)
        print(records[0])
        return [SimpleMatch(**dict(row)) for row in records]

    async def get_by_event(self, event_key: str) -> list[Match]:
        query = """
        SELECT
            matches.key,
            matches.event_key,
            matches.set_number,
            matches.type,
            matches.status,
            red_alliance.teams AS red_alliance_teams,
            red_alliance.dq AS red_alliance_dq,
            red_alliance.backups AS red_alliance_backups,
            blue_alliance.teams AS blue_alliance_teams,
            blue_alliance.dq AS blue_alliance_dq,
            blue_alliance.backups AS blue_alliance_backups,
            matches.time,
            matches.actual_time,
            matches.predicted_time,
            matches.winner,
            matches.video,
            matches.red_breakdown,
            matches.blue_breakdown
        FROM matches
        JOIN
            match_alliances AS red_alliance
            ON matches.key = red_alliance.match_key AND red_alliance.alliance = 'RED'
        JOIN
            match_alliances AS blue_alliance
            ON matches.key = blue_alliance.match_key AND blue_alliance.alliance = 'BLUE'
        WHERE matches.event_key = $1;
        """
        records = await self.db.fetch(query, event_key)
        records = await self.db.fetch(query, event_key)
        if not records:
            raise RuntimeError("Data for matches should exist")
        return []

    async def get_by_team_and_year(self, team_key: str, year: int) -> list[Match]:
        query = """
        SELECT
            matches.key,
            matches.event_key,
            matches.type,
            matches.match_num,
            matches.red_score,
            matches.blue_score,
            matches.completed,
            matches.winner,
            matches.time,
            matches.predicted_time,
            matches.red_breakdown,
            matches.blue_breakdown,
            matches.video,
            red_alliance.teams AS red_alliance_teams,
            blue_alliance.teams AS blue_alliance_teams,
        FROM matches
        JOIN match_alliances ON matches.key = match_alliances.key
        WHERE team.key = $1;
        """
        records = await self.db.fetch(query, team_key, year)
        return [Match(**dict(row)) for row in records]

    async def get_by_team_and_year(self, team_key: str, year: int) -> list[Match]:
        query = """
        SELECT
            matches.key,
            matches.event_key,
            matches.type,
            matches.match_num,
            matches.red_score,
            matches.blue_score,
            matches.completed,
            matches.winner,
            matches.time,
            matches.predicted_time,
            matches.red_breakdown,
            matches.blue_breakdown,
            matches.video,
            red_alliance.teams AS red_alliance_teams,
            blue_alliance.teams AS blue_alliance_teams,
        FROM matches
        JOIN match_alliances ON matches.key = match_alliances.key
        WHERE team.key = $1;
        """
        records = await self.db.fetch(query, team_key, year)
        return [Match(**dict(row)) for row in records]
