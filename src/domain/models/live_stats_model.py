from dataclasses import dataclass

def teste():
    print("teste")
@dataclass()
class LiveStatusModel:

    esportsGameId: str
    esportsMatchId: str
    gameMetadata: str
    frames: str

    @property
    def get_champions_blue_team(self):
        """
        Returns a list with the champions id of the blue team.
        :return: list of champions id.
        """
        champ_list = []
        for champ in self.gameMetadata['blueTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list

    @property
    def get_champions_red_team(self):
        """
        Returns a list with the champions id of the red team.
        :return: list of champions id.
        """
        champ_list = []
        for champ in self.gameMetadata['redTeamMetadata']['participantMetadata']:
            champ_list.append(champ['championId'])
        return champ_list
