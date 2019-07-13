from geohash import Configuration
from geohash.Repository import Repository


class Geohash:
    def __init__(self, configuration: Configuration):
        self.repository = Repository(configuration)
        self.repository.init_datamodel()



