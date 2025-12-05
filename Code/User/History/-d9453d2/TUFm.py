from __future__ import annotations

from datetime import datetime
from enum import Enum

from aiopath import AsyncPath
from devtools import pformat, pprint

from models.webhooks import (
    AllianceSelection,
    AwardsPosted,
    Broadcast,
    CompLevelStarting,
    EventScheduleUpdated,
    MatchScore,
    MessageType,
    Ping,
    UpcomingMatch,
    Verification,
    VideoNotification,
)


class LogLevel(Enum):
    Info = 0
    Warn = 1
    Error = 2
    Fatal = 3


class Logger:
    def __getunixtimestamp(self, now: int) -> int:
        return now - self.starttime

    def __getprefix(self, lvl: LogLevel) -> str:
        match lvl:
            case LogLevel.Info:
                return "INFO: "
            case LogLevel.Warn:
                return "WARN: "
            case LogLevel.Error:
                return "ERROR: "
            case LogLevel.Fatal:
                return "Fatal: "

    def __init__(
        self,
        path: str,
        startime: int,
        logwebhooksasjson: bool = False,
        logtostdout: bool = False,
    ) -> None:
        self.starttime = startime
        self.logfile = AsyncPath(path)
        self.logwebhooksasjson = logwebhooksasjson
        self.logtostdout = logtostdout

    async def log(self, message: str, loglevel: LogLevel) -> None:
        fmessage = f"{self.__getunixtimestamp(int(datetime.now().strftime('%s')))}: {self.__getprefix(loglevel)}{message}"
        if self.logtostdout:
            pprint(fmessage)
        await self.logfile.write_text(fmessage)

    async def log_json(self, data: dict, loglevel: LogLevel) -> None:
        dat = None
        if not self.logwebhooksasjson and data["message_type"] is not None:
            match data["message_type"]:
                case MessageType.UpcomingMatch:
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

            if dat is not None:
                await self.logfile.write_text(pformat(value=dat, highlight=False))
            else:
                dat = "NODAT"
            if self.logtostdout:
                print(pformat(dat, highlight=True))
        if self.logwebhooksasjson:
            fmessage = f"{self.__getunixtimestamp(int(datetime.now().strftime('%s')))}: {self.__getprefix(loglevel)}{dat}"
            await self.logfile.write_bytes(fmessage)
            if self.logtostdout:
                pprint(fmessage)
