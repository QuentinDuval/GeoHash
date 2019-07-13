from geohash.App import *
from geohash.Configuration import *

import random
import string
import time


def with_time(f):
    start_time = time.time()
    res = f()
    print(time.time() - start_time)
    return res


if __name__ == '__main__':
    configuration = Configuration.read_from('configuration.json')
    app = App(configuration=configuration)

    '''
    # app.add_character('a', 10, 15)
    # app.add_character('b', 15, 10)
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    try:
                        x = random.uniform(0, app.map.max_x)
                        y = random.uniform(0, app.map.max_y)
                        app.add_character(a + b + c + d, x, y)
                    except Exception as e:
                        print(e)
    '''

    # print(app.all_characters())
    for _ in range(5):
        print(with_time(lambda: app.find_at(10, 15)))
        print(with_time(lambda: app.find_at_hash(10, 15)))
