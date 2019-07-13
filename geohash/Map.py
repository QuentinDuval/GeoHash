from typing import List, Tuple


class Map:
    CHARS = "0123456789abcdefghijklmnopqrstuv"

    def __init__(self, max_x: float, max_y: float, depth=15):
        self.max_x = max_x
        self.max_y = max_y
        self.depth = depth

    def neighboring_hash(self, x: float, y: float) -> List[str]:
        bits = []
        for bx, by in zip(self.dimension_hash(x, 0, self.max_x),
                          self.dimension_hash(y, 0, self.max_y)):
            bits.extend([bx, by])
        return []   # TODO - just add 1 or 10 or 11, or substract this...

    def get_coord(self, hash: str) -> Tuple[float, float]:
        pass        # TODO - to decode the hash (other way around)

    def get_geohash(self, x: float, y: float):
        bits = []
        for bx, by in zip(self.dimension_hash(x, 0, self.max_x),
                          self.dimension_hash(y, 0, self.max_y)):
            bits.extend([bx, by])
        return self.bits_to_string(bits)

    def dimension_hash(self, val: float, lo: float, hi: float) -> List[int]:
        bits = []
        for _ in range(self.depth):
            mid = lo + (hi - lo) / 2
            if val < mid:
                bits.append(0)
                hi = mid
            else:
                bits.append(1)
                lo = mid
        return bits

    def bits_to_string(self, bits: List[bool]):
        s = ""
        while bits:
            val = 0
            for b in bits[:5]:
                val = (val << 1) + b
            s += self.CHARS[val]
            bits = bits[5:]
        return s
