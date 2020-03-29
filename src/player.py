import pandas as pd
import json

class Player:
    """
    Object for players in SC2 Replay file
    """

    def __init__(self, game, player_number):
        data = game['players'][player_number]
        self.race = data['race']
        self.game_meta_data = self.get_game_meta_data()
        self.build_order = self.get_build_order(data)
        self.opener = self.get_opener(self.build_order)

    def get_game_meta_data(self):
        with open("./resources/game_meta_data.json", 'r') as json_file:
            game_meta_data = json.load(json_file)

            return game_meta_data

    def get_build_order(self, data):
        build_order = pd.DataFrame(data['buildOrder'])
        build_order.loc[:, "time"] = pd.to_datetime(build_order["time"], format="%M:%S").dt.time
        build_order.loc[:, 'identifier'] = build_order['name'].map(self.game_meta_data[self.race])

        return build_order

    def get_opener(self, build_order):
        not_worker = (build_order["is_worker"] == False)
        is_opener = (build_order["time"] < pd.Timestamp("00:06:30").time())
        opener = build_order.loc[not_worker & is_opener]
        opener.reset_index(inplace=True, drop=True)

        return opener