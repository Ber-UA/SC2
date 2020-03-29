from src.player import *

class Game:
    """
    Object for players in SC2 Replay file
    """

    def __init__(self, replay_data):
        self.data = replay_data
        player_1 = Player(self.data, 1)
        player_2 = Player(self.data, 2)
        self.matchup = self.get_matchup([player_1, player_2])
        self.set_race_players([player_1, player_2])


    def get_matchup(self, players):
        matchup = [players[0].race[0], players[1].race[0]]
        matchup.sort()

        return "v".join(matchup)

    def set_race_players(self, players):
        for player in players:
            if player.race == "Protoss":
                self.protoss_player = player
            elif player.race == "Zerg":
                self.zerg_player = player
            elif player.race == "Terran":
                self.terran_player = player
