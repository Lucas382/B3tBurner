from src.domain.models.player_model import PlayerModel
from src.infrastructure.utils.api_utils import get_api_data
from src.infrastructure.utils.json_file_utils import is_file_exists, save_file_data, get_file_data


class PlayerDataService:

    @classmethod
    def get_players_model_by_name(cls, player_name: str):
        player_name = player_name.capitalize()
        data = cls.get_players_data_file(player_name)
        model = PlayerModel(**data)

        return model

    @classmethod
    def get_players_data_file(cls, player_name: str) -> dict:
        """
        Retrieves the player data by name.
        :param player_name: The name of the player.
        :return (dict): The player data.
        """
        # Implement the logic to obtain player data, including API interaction, file handling, etc.
        # You can use the existing logic from the `get_players_data_file` function

        if not is_file_exists(folder='players', file_name=player_name):
            data = {
                'playerData': get_api_data('player_data_url', 'oracle_header', player_name),
                'recentGames': get_api_data('player_game_details_url', 'oracle_header', player_name),
                'splitStats': get_api_data('player_stats_split_url', 'oracle_header', player_name),
                'championPool': get_api_data('player_pool_url', 'oracle_header', player_name, param=player_name)
            }

            save_file_data(data, 'players', player_name)
        else:
            data = get_file_data(folder='players', file_name=player_name)

        return data
