from geohash import Configuration
from geohash.Map import Map
from geohash.Repository import Repository


class App:
    def __init__(self, configuration: Configuration):
        self.repository = Repository(configuration)
        self.repository.init_datamodel()
        self.map = Map(max_x=20, max_y=40, depth=15)

    def add_character(self, name: str, x: float, y: float):
        self.repository.add_character(name, x, y, self.map)

    def all_characters(self):
        return self.repository.all_characters()

    def find_at(self, x: float, y: float):
        return self.repository.find_at(x, y)

    def find_at_hash(self, x: float, y: float):
        return self.repository.find_at_hash(x, y, self.map)

