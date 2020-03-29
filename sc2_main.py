import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.read_data import *
from src.game import *
from src.create_features import *
from src.feature_encoder import *
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

data = ReplayData()
games = [Game(game) for game in data.replays]

protoss = [game.protoss_player.opener for game in games if game.matchup == "PvZ"]
features = [CreateFeatures().predict(item) for item in protoss]
features = pd.DataFrame(features)

encoded_features = pd.DataFrame(FeatureEncoder().encode(features))

clustering_data = features.loc[:, [column for column in features.columns if re.search(".*Counts$", column)]]
clustering_data = clustering_data.merge(encoded_features, left_index=True, right_index=True)

dendogram = sch.dendrogram(sch.linkage(encoded_features.values, method='ward'))
plt.title('Dendogram')
plt.xlabel("Games")
plt.ylabel("Distances")
plt.show()

hc = AgglomerativeClustering(n_clusters=8, affinity="euclidean", linkage='ward')
results = hc.fit_predict(encoded_features.values)

features.loc[:, "labels"] = results
features.sort_values('labels', inplace=True)

terran = [game.terran_player.opener for game in games if game.matchup == "TvZ"]
zerg = [game.zerg_player.opener for game in games if game.matchup in ["PvZ", "TvZ"]]

