from src.domain.models.match_schedule_model import MatchScheduleModel
from src.infrastructure.utils.api_utils import get_api_data
from src.infrastructure.utils.datetime_utils import string_to_date
from src.infrastructure.utils.json_file_utils import is_file_exists, save_file_data, get_file_data


class MatchScheduleService:

    @classmethod
    def get_match_schedule_data_file(cls) -> dict:
        """
        Retrieves the match schedule data.
        :return (dict) : The match schedule data.
        """
        if not is_file_exists(folder='games', file_name='match_schedule'):
            data = get_api_data('match_schedule_url', 'esports_header')
            save_file_data(data, 'games', 'match_schedule')
        else:
            data = get_file_data(folder='games', file_name='match_schedule')

        return data

    @classmethod
    def extract_match_schedule_events(cls, match_schedule_data: dict) -> list[MatchScheduleModel]:
        """
        Extracts match schedule events from match schedule data
        :param (dict) match_schedule_data : The match schedule data to extract
        :return list[MatchScheduleModel]: A list of a match representation (MatchScheduleModel)
        """
        events = match_schedule_data.get('data', {}).get('schedule', {}).get('events', [])
        matches = []
        for event in events:
            if all(key in event for key in MatchScheduleModel.get_all_attrs_names()):
                matches.append(MatchScheduleModel(**event))

        return matches

    @classmethod
    def filter_matches_by_timestamp_and_league(cls, matches: list[MatchScheduleModel], iso_timestamp: str, league: str) -> \
    list[MatchScheduleModel]:
        """
        Returns a list of matches filtered by day and league
        :param matches:
        :param iso_timestamp:
        :param league:
        :return list[MatchScheduleModel]:
        """
        return [match for match in matches if
                string_to_date(match.startTime).day == string_to_date(iso_timestamp).day and
                match.league.name == league]

