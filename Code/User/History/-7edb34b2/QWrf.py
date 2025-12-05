
class UpcomingMatchMessageData(BaseModel):
    event_key: str
    match_key: str
    event_name: str
    team_keys: list[str]
    scheduled_time: int | None # I <3 unix
    predicted_time: int | None # I <3 unix
    webcast: Webcast | None


class UpcomingMatch(BaseModel):
    message_data: UpcomingMatchMessageData
    message_type: str

class Blue(BaseModel):
    score: int
    teams: list[str]


class Red(BaseModel):
    score: int
    teams: list[str]


class Alliances(BaseModel):
    blue: Blue
    red: Red


class Match(BaseModel):
    comp_level: str
    match_number: int
    videos: list[str]
    time_string: str
    set_number: int
    key: str
    time: int
    score_breakdown: None # this is null in the docs???
    alliances: Alliances
    event_key: str


class MatchScoreMessageData(BaseModel):
    event_name: str
    match: Match


class MatchScore(BaseModel):
    message_data: MatchScoreMessageData
    message_type: str

class Video(BaseModel):
    key: str
    type: str


class VideoNotificationMessageData(BaseModel):
    event_name: str
    match: Match


class VideoNotification(BaseModel):
    message_data: VideoNotificationMessageData
    message_type: str

class CompLevelStartingMessageData(BaseModel):
    event_name: str
    comp_level: str
    event_key: str
    scheduled_time: int


class CompLevelStarting(BaseModel):
    message_data: CompLevelStartingMessageData
    message_type: str

class District(BaseModel):
    abbreviation: str
    display_name: str
    key: str
    year: int


class Webcast(BaseModel):
    channel: str
    file: str
    castype: str


class Event(BaseModel):
    address: str
    city: str
    country: str
    district: District
    division_keys: list
    end_date: str
    event_code: str
    event_type: int
    event_type_string: str
    first_event_code: str
    first_event_id: str
    gmaps_place_id: str
    gmaps_url: str
    key: str
    lat: float
    lng: float
    location_name: str
    name: str
    parent_event_key: None # ??? 
    playoff_type: None # ???
    playoff_type_string: None # ???
    postal_code: str
    short_name: str
    start_date: str
    state_prov: str
    timezone: str
    webcasts: list[Webcast]
    website: str
    week: int
    year: int


class AllianceSelectionMessageData(BaseModel):
    event_name: str
    event_key: str
    event: Event


class AllianceSelection(BaseModel):
    message_data: AllianceSelectionMessageData
    message_type: str

class Recipient(BaseModel):
    team_number: int
    awardee: None # ???


class Award(BaseModel):
    event_key: str
    award_type: int
    name: str
    recipient_list: list[Recipient]
    year: int


class AwardsPostedMessageData(BaseModel):
    event_key: str
    event_name: str
    awards: list[Award]


class AwardsPosted(BaseModel):
    message_data: AwardsPostedMessageData
    message_type: str

class EventScheduleUpdatedMessageData(BaseModel):
    event_key: str
    event_name: str
    first_match_time: int

class EventScheduleUpdated(BaseModel):
    message_data: EventScheduleUpdatedMessageData
    message_type: str

class PingMessageData(BaseModel):
    title: str
    desc: str


class Ping(BaseModel):
    message_data: PingMessageData
    message_type: str


class BroadcastMessageData(BaseModel):
    title: str
    desc: str
    url: str


class Broadcast(BaseModel):
    message_data: BroadcastMessageData
    message_type: str

class VerificationMessageData(BaseModel):
    verification_key: str


class Verification(BaseModel):
    message_data: VerificationMessageData
    message_type: str
