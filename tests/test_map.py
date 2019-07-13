from geohash.Map import Map


def test_map():
    map = Map(max_x=10, max_y=20, depth=15)
    assert "000000" == map.get_geohash(0, 0)
    assert "vvvvvv" == map.get_geohash(10, 20)
    assert "cu3of1" == map.get_geohash(3.5, 14)
