from src.domain.models.match_schedule_model import MatchScheduleModel
from src.domain.protocols.match_schedule_protocol import MatchScheduleProtocol
from src.domain.services.match_schedule_service import MatchScheduleService
from src.infrastructure.utils.datetime_utils import get_rounded_iso_timestamp


class LiveDetailsService:

    @classmethod
    def get_today_matches_by_league(cls, league: str) -> list[MatchScheduleModel]:
        """
        Returns a list of matches filtered by day and league
        :param league: The league name to filter by
        :return list[MatchScheduleModel]: A list of a match representation (MatchScheduleModel)
        """
        iso_timestamp = get_rounded_iso_timestamp()
        match_schedule_protocol: MatchScheduleProtocol = MatchScheduleService()
        match_schedule_data = match_schedule_protocol.get_match_schedule_data_file()
        match_events = match_schedule_protocol.extract_match_schedule_events(match_schedule_data)
        matches = match_schedule_protocol.filter_matches_by_timestamp_and_league(match_events, iso_timestamp, league.upper())

        return matches

