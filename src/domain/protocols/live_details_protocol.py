from src.domain.models.match_schedule_model import MatchScheduleModel
from typing import Protocol


class LiveDetailsServiceProtocol(Protocol):

    def get_today_matches_by_league(self, league: str) -> list[MatchScheduleModel]:
        ...
