#lruCache
import logging
class lruCache:
    __cacheSize = 3
    __cacheHit = 0
    __cacheMiss = 0
    cache = {}
    def __init__(self):
        logging.debug("CLASS lruCache:__init__,cacheSize={}".format(self.__cacheSize))
        logging.debug("CLASS lruCache:__init__,cacheHit={}".format(self.__cacheHit))
        logging.debug("CLASS lruCache:__init__,cacheMiss={}".format(self.__cacheMiss))
        #pre-popluating keys is in-efficient
        #self.cache = {key: None for key in range(self.__cacheSize)}
        logging.debug("CLASS lruCache:__init__,cache={}".format(self.cache))
    def __checkCache(self,page):
        logging.debug("CLASS lruCache:__checkCache,page={}".format(page))
        if page in self.cache.values():
            logging.debug("CLASS lruCache:__checkCache-->HIT,page={}".format(page))
            return True
        else:
            logging.debug("CLASS lruCache:__checkCache-->MISS,page={}".format(page))
            return False

