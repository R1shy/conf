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
    match data["message_type"]:
                case MessageType.UpcomingMatch.value:
                    dat = UpcomingMatch(
                        message_data=data["message_data"],
                        message_type=data["message_data"],
                    )
                case MessageType.MatchScore.value:
                    dat = MatchScore(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.MatchVideo.value:
                    dat = VideoNotification(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.CompLevelStarting.value:
                    dat = CompLevelStarting(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.AllianceSelection.value:
                    dat = AllianceSelection(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.AwardsPosted.value:
                    dat = AwardsPosted(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.EventScheduleUpdated.value:
                    dat = EventScheduleUpdated(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.Ping.value:
                    dat = Ping(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.Broadcast.value:
                    dat = Broadcast(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
                case MessageType.Verification.value:
                    dat = Verification(
                        message_data=data["message_data"],
                        message_type=data["message_type"],
                    )
    return 200  # 200 or prune
