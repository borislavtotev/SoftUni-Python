import json
from .base import Loader


class JSONLoader(Loader):

    def load(self):
        with open(self.filename) as f:
            input_data = json.load(f)
            return input_data

