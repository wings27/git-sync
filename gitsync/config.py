"""git-sync config"""

__author__ = 'wenqiushi'

import yaml


class Config:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = "../config/mapping.yml"

        self.__pathMapping = self.load_config(config_path)

    @staticmethod
    def process_config(config):
        mapping_def = config['def']
        mapping = config['mapping']
        for profile in mapping:
            for old_key in list(mapping[profile].keys()):
                new_key = mapping_def[old_key]
                mapping[profile][new_key] = mapping[profile].pop(old_key)
        return mapping

    def load_config(self, config_path):
        with open(config_path, 'r') as stream:
            return self.process_config(yaml.load(stream))

    def view_path_mapping(self):
        return self.__pathMapping.copy()
