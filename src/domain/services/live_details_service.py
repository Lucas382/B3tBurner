from src.domain.models.match_schedule_model import MatchScheduleModel
from src.infrastructure.utils.datetime_utils import get_rounded_iso_timestamp, string_to_date
from src.infrastructure.utils.match_file_utils import get_match_schedule_data


def filter_matches_by_timestamp_and_league(matches: list[MatchScheduleModel], iso_timestamp: str, league: str) -> list[MatchScheduleModel]:
    """
    Returns a list of matches filtered by day and league
    :param matches:
    :param iso_timestamp:
    :param league:
    :return list[MatchScheduleModel]:
    """
    return [match for match in matches if string_to_date(match.startTime).day == string_to_date(iso_timestamp).day and
            match.league.name == league]


def extract_match_schedule_events(match_schedule_data: dict) -> list[MatchScheduleModel]:
    """
    Extracts match schedule events from match schedule data
    :param (dict) match_schedule_data : The match schedule data to extract
    :return list[MatchScheduleModel]: A list of a match representation (MatchScheduleModel)
    """
    events = match_schedule_data.get('data', {}).get('schedule', {}).get('events', [])
    matchs = []
    for event in events:
        if all(key in event for key in MatchScheduleModel.get_all_attrs_names()):
            matchs.append(MatchScheduleModel(**event))

    return matchs


class LiveDetailsService:

    @classmethod
    def get_today_matches_by_league(cls, league: str) -> list[MatchScheduleModel]:
        """
        Returns a list of matches filtered by day and league
        :param league: The league name to filter by
        :return list[MatchScheduleModel]: A list of a match representation (MatchScheduleModel)
        """
        iso_timestamp = get_rounded_iso_timestamp()
        match_schedule_data = get_match_schedule_data()
        match_events = extract_match_schedule_events(match_schedule_data)
        matches = filter_matches_by_timestamp_and_league(match_events, iso_timestamp, league.upper())

        return matches
