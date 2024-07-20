#!/usr/bin/python3
"""a class FIFOCache that inherits from BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache method"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.load = []

    def put(self, key, item):
        """put function"""
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            elif len(self.cache_data.keys()) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.load.append(key)
            else:
                self.cache_data[key] = item
                discard = self.load[0]
                del self.cache_data[self.load[0]], self.load[0]
                self.load.append(key)
                print(f'DISCARD: {discard}')

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key, None)
