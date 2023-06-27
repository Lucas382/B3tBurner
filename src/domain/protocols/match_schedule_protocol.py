from typing import Protocol

from src.domain.models.match_schedule_model import MatchScheduleModel


class MatchScheduleProtocol(Protocol):
    def get_match_schedule_data_file(self) -> dict:
        ...

    def extract_match_schedule_events(self, match_schedule_data: dict) -> list[MatchScheduleModel]:
        ...

    def filter_matches_by_timestamp_and_league(self, matches: list[MatchScheduleModel], iso_timestamp: str, league: str) -> \
    list[MatchScheduleModel]:
        ...
