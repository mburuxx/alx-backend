#!/usr/bin/python3
"""a class BasicCache that inherits from BaseCaching and is a caching system"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache"""

    def put(self, key, item):
        """put function"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key:
            return self.cache_data.get(key, None)
