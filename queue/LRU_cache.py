"""
Implementation of LRU cache

Time complexity : 

access worst case O(N)

Space complexity: O(N)

"""

import time
from collections import OrderedDict

class LRU_USING_NORMAL_DICT():

    SIZE = 5

    def __init__(self):
        self.cache = dict()

    def get(self, key):
        return self.cache[key]["value"]

    def put(self, key, val):
        if len(self.cache) >= LRU.SIZE:
            print("size exeeds")

            min_ts = time.time()
            min_key = -1
            for k, v in self.cache.items():
                if v["ts"] < min_ts:
                    min_key, min_ts = k, v["ts"]

            print("min key {} , value  {}".format(min_key, min_ts))
            print("deleteing least recently used")
            del self.cache[min_key]

        print("puting value")
        self.cache[key] = {"value": val, "ts": time.time()}

"""

LRU cache implementation based on Ordered Dict.

Ordered Dict can preserve the order of insertion, 
and it has specialized methods that supports reordering

"""
class LRU():

    SIZE=5

    def __init__(self):

        self.cache = OrderedDict()

    def get(self,key):
        value = self.cache.__getitem__(key)
        # Moving the recently accesed item to right end
        self.cache.move_to_end(key)
        return value


    def put(self,key,value):

        self.cache[key] = value

        if len(self.cache) > LRU.SIZE :
            # Deleting the first element, which will be least used
            oldest_item = next(iter(self.cache.keys()))
            del self.cache[oldest_item]


if __name__ == "__main__":

    lru = LRU()
    lru.put(1, "hello1")
    lru.put(2, "hello2")
    lru.put(3, "hello3")
    lru.put(4, "hello4")
    lru.put(5, "hello5")
    lru.put(6, "hello6")
    lru.put(7, "hello7")

    print(lru.get(4))
    print(lru.__dict__)
