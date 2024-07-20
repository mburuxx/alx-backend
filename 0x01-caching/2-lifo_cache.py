#!/usr/bin/python3
"""a class LIFOCache that inherits from BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache method"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.key = ""

    def put(self, key, item):
        """put function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                del self.cache_data[self.key]
                print(f'DISCARD: {self.key}')
            self.key = key

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key, None)
