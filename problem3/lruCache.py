#lruCache
import logging
class lruCache:
    __cacheSize = 3
    __cacheHit = 0
    __cacheMiss = 0
    cache = list()
    def __init__(self):
        logging.debug("CLASS lruCache:__init__,cacheSize={}".format(self.__cacheSize))
        logging.debug("CLASS lruCache:__init__,cacheHit={}".format(self.__cacheHit))
        logging.debug("CLASS lruCache:__init__,cacheMiss={}".format(self.__cacheMiss))
        #pre-popluating keys is in-efficient
        #self.cache = {key: None for key in range(self.__cacheSize)}
        logging.debug("CLASS lruCache:__init__,cache={}".format(self.cache))
    def __checkCache(self,page):
        logging.debug("CLASS lruCache:__checkCache,page={}".format(page))
        if page in self.cache:
            logging.debug("CLASS lruCache:__checkCache-->HIT,page={}".format(page))
            return True
        else:
            logging.debug("CLASS lruCache:__checkCache-->MISS,page={}".format(page))
            return False
    def __delete(self,element=None,pos=None):
        logging.debug("CLASS lruCache:__delete,element={},pos={}".format(element,pos))
        condition1 = (pos == None)
        condition2 = (element != None)
        if condition1 and condition2:
            cacheIndex = self.cache[element]
            del self.cache[cacheIndex]
            logging.debug("CLASS lruCache:__delete,element={},pos={}".format(element,cacheIndex))
        else:
            self.cache.pop()
            logging.debug("CLASS lruCache:__delete,element={},pos={}".format(element,self.__cacheSize-1))
    def __insert(self,element):
        logging.debug("CLASS lruCache:__insert,element={}".format(element))
        self.cache.insert(0,element)
    def __add(self,element):
        logging.debug("CLASS lruCache:__add,element={}".format(element))
        condition1 = (len(self.cache)<self.__cacheSize)
        if(condition1):
            self.__insert(element)
        else:
            self.__delete()
            self.__insert(element)
    def deleteAndInsert(self,page):
        logging.debug("CLASS lruCache:deleteAndInsert,page={}".format(page))
        
    """def add(self,page):
        logging.debug("CLASS lruCache:add,page={}".format(page))
        if self.__checkCache(page):
            """