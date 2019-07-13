from geohash.App import *
from geohash.Configuration import *


if __name__ == '__main__':
    configuration = Configuration.read_from('configuration.json')
    app = App(configuration=configuration)
    # app.add_character('a', 10, 15)
    # app.add_character('b', 15, 10)
    print(app.all_characters())
    print(app.find_at(10, 15))
    print(app.find_at_hash(10, 15))
