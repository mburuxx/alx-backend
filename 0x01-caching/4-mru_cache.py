#!/usr/bin/python3
"""a class MRUCache that inherits from BaseCaching and is a caching system"""


from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache method"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.load = deque()

    def put(self, key, item):
        """put function"""
        if key and item:
            if key in self.cache_data:
                self.load.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                popped = self.load.pop()
                del self.cache_data[popped]
                print("DISCARD: " + str(popped))
            self.load.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            self.load.remove(key)
            self.load.append(key)
            return self.cache_data.get(key, None)
