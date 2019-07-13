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
    app.add_character('a', 10, 15)
    app.add_character('b', 15, 10)
    app.add_character('c', 5, 20)
    app.add_character('d', 2, 30)
    app.add_character('e', 2, 30)
    app.add_character('f', 2, 31)
    app.add_character('g', 2, 32)
    app.add_character('h', 2, 33)
    app.add_character('i', 2, 34)
    app.add_character('j', 2, 35)
    app.add_character('k', 2, 36)
    
    
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

    for _ in range(5):
        print('-' * 50)

        print(with_time(lambda: app.find_at(10, 15)))
        print(with_time(lambda: app.find_at(15, 10)))
        print(with_time(lambda: app.find_around(2, 30)))

        print(with_time(lambda: app.find_at_hash(10, 15)))
        print(with_time(lambda: app.find_at_hash(15, 10)))
        print(with_time(lambda: app.find_around_hash(2, 30)))

