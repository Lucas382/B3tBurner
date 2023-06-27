from dataclasses import dataclass
from typing import List

@dataclass
class RecentGame:
    gameId: str
    assists: int
    blueTag: str
    bluebot: str
    bluejng: str
    bluemid: str
    bluesup: str
    bluetop: str
    cspm: float
    deaths: int
    dpm: int
    gameCreation: str
    gameInMatch: str
    kills: int
    kp: str
    matchId: str
    oeGameId: str
    opponentLogo: str
    opponentTeam: str
    opponentTeamId: str
    opponentTeamTag: str
    ownTeamId: str
    ownTeamName: str
    ownTeamTag: str
    patch: float
    playerChampion: str
    playerId: str
    playerName: str
    playerPosition: str
    redTag: str
    redbot: str
    redjng: str
    redmid: str
    redsup: str
    redtop: str
    result: int
    side: str
    tournament: str
    vod: str
    wpm: float


@dataclass
class ChampionPool:
    Champion: str
    Pos: str
    GP: int
    Wpct: str
    BLNDpct: str
    KDA: int
    KP: str
    DTHpct: str
    CSPM: float
    DMGpct: str
    DPM: int
    GD10: int
    GOLDpct: str
    WCPM: float
    WPM: float
    XPD10: int


@dataclass
class SplitStatsModel:
    Event: str
    Team: str
    Pos: str
    GP: int
    Wpct: str
    KDA: float
    KP: str
    CSPM: float
    DMGpct: str
    DPM: int
    DTHpct: str
    GD10: int
    GOLDpct: str
    WCPM: float
    WPM: float
    XPD10: int

@dataclass
class PlayerData:
    playerId: str
    name: str
    realName: str
    position: str
    age: int
    birthdate: str
    contractEnd: str
    gamepediaLink: str
    isRetired: int
    league: str
    playerPhoto: str
    residency: str
    teamId: str
    teamLogo: str
    teamName: str
    teamTag: str

@dataclass
class PlayerModel:
    playerData: PlayerData
    splitStats: List[SplitStatsModel]
    championPool: List[ChampionPool]
    recentGames: List[RecentGame]

    def __post_init__(self):
        self.playerData = PlayerData(**self.playerData)
        split_stats_list = []
        for split_stats in self.splitStats:
            for attr_name in ['W%', 'DMG%', 'DTH%', 'GOLD%']:
                pct_value = split_stats.pop(attr_name)  # Retrieve and remove the percentage attribute
                attr_name_adjusted = attr_name.replace('%', 'pct')  # Adjusted attribute name
                split_stats[attr_name_adjusted] = pct_value  # Assign the value to the adjusted attribute name
            split_stats_list.append(SplitStatsModel(**split_stats))
        self.splitStats = split_stats_list

        champion_pool_list = []
        for champion_pool in self.championPool:
            for attr_name in ['W%', 'BLND%', 'DMG%', 'DTH%', 'GOLD%']:
                pct_value = champion_pool.pop(attr_name)
                attr_name_adjusted = attr_name.replace('%', 'pct')
                champion_pool[attr_name_adjusted] = pct_value
            champion_pool_list.append(ChampionPool(**champion_pool))
        self.championPool = champion_pool_list

        self.recentGames = [RecentGame(**recentGames) for recentGames in self.recentGames]



