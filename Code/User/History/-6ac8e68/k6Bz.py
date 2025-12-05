from datetime import datetime
from core import AppCore
from models.matches import Match
from tba.constants import EventType
from tba.utils import get_district, get_state_prov


class TBAClient:
    def __init__(self, app: AppCore) -> None:
        self.api_url = "https://www.thebluealliance.com/api/v3/"
        self.session = app.session
        self.api_key = app.config.TBA_API_KEY

    def _map_team_to_db(self, tba_data: dict) -> tuple:
        return (
            tba_data["key"],
            tba_data["team_number"],
            tba_data["nickname"],
            tba_data["rookie_year"],
            "NA",  # district
            tba_data.get("city"),
            get_state_prov(tba_data["state_prov"]),
            tba_data["country"],
        )

    def _map_event_to_db(self, tba_data: dict) -> tuple:
        district_data: dict = tba_data["district"] or {}
        district = district_data.get("abbreviation", None)

        event_type = EventType(tba_data["event_type"])

        if event_type.is_champs:
            tba_data["week"] = 8
        elif event_type.is_offseason:
            tba_data["week"] = 9

        return (
            tba_data["key"],
            tba_data["name"],
            tba_data["event_type"],
            tba_data["week"],
            tba_data["year"],
            datetime.strptime(tba_data["start_date"], "%Y-%m-%d").date(),
            datetime.strptime(tba_data["end_date"], "%Y-%m-%d").date(),
            get_district(district),
            tba_data["city"],
            get_state_prov(tba_data["state_prov"]),
            tba_data["country"],
        )

    def _map_match_to_db(self, tba_data: dict) -> Match:
        local_completed = False
        time = tba_data["time"]
        predicted_time = tba_data["predicted_time"]
        if tba_data["actual_time"]:
            local_completed = True

        video = ""
        videos_list: list[dict[str, str]] = tba_data["videos"]
        if predicted_time is None:
            predicted_time = 0
        if time is None:
            time = 0
        for item in videos_list:
            if item.get("type") == "youtube":
                video = item.get("key")
                break

        return (
            tba_data["key"],
            tba_data["event_key"],
            tba_data["comp_level"],
            tba_data["match_number"],
            tba_data["alliances"]["red"]["score"],
            tba_data["alliances"]["blue"]["score"],
            completed,
            tba_data["winning_alliance"],
            time,
            predicted_time,
            breakdown.get("red", {}),
            breakdown.get("blue", {}),
            video,
        )

    def _map_alliance_to_db(self, tba_data: dict, color: str, idx: int) -> tuple:
        return (
            tba_data["key"],
            tba_data["alliances"][color]["team_keys"][idx],
            color,
            idx + 1,
            int(tba_data["event_key"][0:4]),
        )

    async def _tba_api_dict(self, endpoint: str) -> list[dict] | None:
        headers = {"X-TBA-Auth-Key": self.api_key}

        timeout = aiohttp.ClientTimeout(total=20)

        out_json: list[dict] | None = None

        async with self.session.get(
            self.api_url + endpoint, headers=headers, timeout=timeout
        ) as response:
            if response.status == 304:
                # TODO: Handle ETag
                pass
            elif response.status == 200:
                out_json = await response.json()
            else:
                response.raise_for_status()

        return out_json

    async def _tba_api_str(self, endpoint: str) -> list[str] | None:
        headers = {"X-TBA-Auth-Key": self.api_key}

        timeout = aiohttp.ClientTimeout(total=20)

        out_json: list[str] | None = None

        async with self.session.get(
            self.api_url + endpoint, headers=headers, timeout=timeout
        ) as response:
            if response.status == 304:
                # TODO: Handle ETag
                pass
            elif response.status == 200:
                out_json = await response.json()
            else:
                response.raise_for_status()

        return out_json

    async def fetch_teams(self) -> list[tuple]:
        teams = []

        for i in range(30):
            endpoint = f"teams/{str(i)}"

            try:
                team_json = await self._tba_api_dict(endpoint)
            except aiohttp.ClientResponseError:
                # TODO: log
                raise

            if team_json is None:
                # TODO: log
                break

            for team_dict in team_json:
                teams.append(self._map_team_to_db(team_dict))

        return teams

    async def fetch_events(self, year: int) -> list[tuple]:
        events = []

        endpoint = "events/" + str(year)

        try:
            event_json = await self._tba_api_dict(endpoint)
        except aiohttp.ClientResponseError:
            # TODO: log
            raise

        if event_json is None:
            # TODO: log
            return []

        for event_dict in event_json:
            # Filter out preseason events
            if event_dict["event_type"] < 100:
                events.append(self._map_event_to_db(event_dict))

        return events

    async def fetch_matches(
        self, event_keys: list[str]
    ) -> tuple[list[tuple], list[tuple]]:
        matches = []
        alliances = []

        for event_key in event_keys:
            endpoint = f"event/{event_key}/matches"

            try:
                match_json = await self._tba_api_dict(endpoint)
            except aiohttp.ClientResponseError:
                # TODO: log
                raise

            if match_json is None:
                # TODO: log
                continue

            for match_dict in match_json:
                matches.append(self._map_match_to_db(match_dict))

                for color in ["red", "blue"]:
                    for idx in range(3):
                        alliances.append(
                            self._map_alliance_to_db(match_dict, color, idx)
                        )

        return matches, alliances

    async def fetch_team_events(self, event_keys: list[str], year: int) -> list[tuple]:
        team_events = []

        for event_key in event_keys:
            endpoint = f"event/{event_key}/teams/keys"

            try:
                team_event_keys = await self._tba_api_str(endpoint)
            except aiohttp.ClientResponseError:
                raise

            if team_event_keys is None:
                # TODO: log
                continue

            for team_key in team_event_keys:
                team_events.append((team_key, event_key, year))

        return team_events
