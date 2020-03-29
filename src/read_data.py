import glob
import os
import spawningtool.parser as sc2parser
import pickle


class ReplayData:
    """
    Read folder with SC2 Replay Data
    """

    def __init__(self):
        if os.path.exists("./resources/replay_data.pkl"):
            self.replays = self.read_replay_files()
        else:
            self.replays = self.parse_replay_files()

    def parse_replay_files(self):
        replay_files = glob.glob('./replay_data/**/*.SC2Replay')
        replays = [sc2parser.parse_replay(file) for file in replay_files]
        with open("./resources/replay_data.pkl", "wb") as file:
            pickle.dump(replays, file)

        return replays

    def read_replay_files(self):
        with open("./resources/replay_data.pkl", "rb") as file:
            replays = pickle.load(file)

        return replays