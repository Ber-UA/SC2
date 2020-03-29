import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class FeatureEncoder:
    def __init__(self):
        self.label_encoder = LabelEncoder()
        self.one_hot_encoder = OneHotEncoder()

    def encode(self, data):
        self.cols_to_encode = [column for column in data.columns if re.search(r".*(Research|Tech)$", column)]
        to_encode = data.loc[:, self.cols_to_encode].values

        for i in range(0, to_encode.shape[1]):
            to_encode[:, i] = self.label_encoder.fit_transform(to_encode[:, i])
        output = self.one_hot_encoder.fit_transform(to_encode).toarray()

        return output