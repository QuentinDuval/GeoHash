from geohash.Geohash import *


if __name__ == '__main__':
    configuration = Configuration.read_from('configuration.json')
    app = Geohash(configuration=configuration)
