import json
import pandas as pd


class CreateFeatures:
    """
    Docstring
    """

    def __init__(self):
        self.features = {}

    def predict(self, data):
        self.features["TechStructureCounts"] = self.tech_structure_counts(data)
        #self.features["EconomyStructureCounts"] = self.economy_structure_counts(data)
        self.features["DefensiveStructureCounts"] = self.defensive_structure_counts(data)
        self.features["GasCounts"] = self.gas_counts(data)
        #self.features["BaseCounts"] = self.base_counts(data)
        self.features["SecondTech"] = self.tech_structure(data, 2)
        self.features["ThirdTech"] = self.tech_structure(data, 3)
        self.features["FourthTech"] = self.tech_structure(data, 4)
        self.features["FifthTech"] = self.tech_structure(data, 5)
        #self.features["FirstResearch"] = self.research(data, 1)
        self.features["SecondResearch"] = self.research(data, 2)
        self.features["ThirdResearch"] = self.research(data, 3)

        return self.features

    def tech_structure_counts(self, data):
        counts = data.loc[data['identifier'].isin(['TechStructure']), 'identifier'].count()
        return counts

    def economy_structure_counts(self, data):
        counts = data.loc[data['identifier'].isin(['EconomyStructure']), 'identifier'].size
        return counts

    def defensive_structure_counts(self, data):
        counts = data.loc[data['identifier'].isin(['DefensiveStructure']), 'identifier'].size
        return counts

    def gas_counts(self, data):
        counts = data.loc[data['name'].isin(['Assimilator', "Refinery", "Extractor"]), 'name'].size
        return counts

    def base_counts(self, data):
        counts = data.loc[data['name'].isin(['Nexus', "CommandCenter", "Hatchery"]), 'name'].size
        return counts

    def tech_structure(self, data, n):
        tech = data.loc[data['identifier'].isin(['TechStructure'])]
        tech.reset_index(inplace=True, drop=True)
        if tech.index.size >= n:
            tech = tech.loc[(n - 1), 'name']
        else:
            tech = "None"
        return tech

    def research(self, data, n):
        research = data.loc[data['identifier'].isin(['Research'])]
        research.reset_index(inplace=True, drop=True)
        if research.index.size >= n:
            research = research.loc[(n - 1), 'name']
        else:
            research = "None"
        return research