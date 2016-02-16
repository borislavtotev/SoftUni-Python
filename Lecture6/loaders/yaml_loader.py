import yaml

from .base import Loader


class YAMLLoader(Loader):

        def load(self):
            with open(self.filename) as f:
                input_data = yaml.load(f)
                return input_data

