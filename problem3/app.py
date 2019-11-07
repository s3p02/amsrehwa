from flask import Flask
from flask import request
from flask import abort
import logging
import sys
import collections
instanceIp=''
app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

class lruCache:
    __cacheSize = 3000
    hitCount = 0
    missCount = 0
    lruc = None
    #pagesDict = {}
    def __init__(self):
        print("LRU CACHE")
        self.lruc = collections.deque(maxlen=self.__cacheSize)
        print("CLASS lruCache:__init__,lruc: {}".format(self.lruc))
    
    def checkCache(self,page):
        if page in self.lruc:
            indexOfPage = self.lruc.index(page)
            if indexOfPage == 0:
                self.inc("hit")
                return page
            else:
                del self.lruc[indexOfPage]
                self.lruc.appendleft(page)
                self.inc("hit")
                return page
        else:
            #url = "http://127.0.0.1:38080/example-URL"
            self.lruc.appendleft(page)
            #self.pagesDict[page] = url
            self.inc("miss")
            return page

    def inc(self,option):
        if option == "hit":
            prev = self.hitCount
            logging.debug("CLASS lruCache:inc:incHit,prev: {}".format(prev))
            self.hitCount += 1
            curr = self.hitCount
            logging.debug("CLASS lruCache:inc:incHit,curr: {}".format(curr))
        elif option == "miss":
            prev = self.missCount
            logging.debug("CLASS lruCache:inc:incMiss,prev: {}".format(prev))
            self.missCount += 1
            curr = self.missCount
            logging.debug("CLASS lruCache:inc:incMiss,curr: {}".format(curr))
    
    def clearHit(self):
        print("CLASS lruCache:clearHit,Prev: {}".format(self.hitCount))
        self.hitCount = 0
        print("CLASS lruCache:clearHit,Current: {}".format(self.hitCount))
    
    def clearMiss(self):
        print("CLASS lruCache:clearHit,Prev: {}".format(self.missCount))
        self.missCount = 0
        print("CLASS lruCache:clearHit,Current: {}".format(self.missCount))

a = lruCache()

@app.route('/')
def info():
    _info = '''
    <h1>Sample for Application Endpoint is :- http://{0}:38080/example-route?lat=90&lng=180</h1>
    <h1>-90 >= lat <=90 & -180 >= lng <=180 </h1>
    <h1>Check Cache:- http://{0}:38080/showCache</h1>
    <h1>Check Hit Count:- http://{0}:38080/getHit</h1>
    <h1>Check Miss Count:- http://{0}:38080/getMiss</h1>
    <h1>Clear Hit Count:- http://{0}:38080/clearHit</h1>
    <h1>Clear Miss Count:- http://{0}:38080/clearMiss</h1>
    '''.format(instanceIp)
    return _info

@app.route('/showCache')
def showCache():
    curr = a.lruc
    #currPages = a.pagesDict
    showCacheMessage = '''<h1>Cur Cache: {}</h1>'''.format(curr)
    #<h1>Cur CachePages: {}</h1>'''.format(curr,currPages)
    return showCacheMessage

@app.route('/clearHit')
def clearHit():
    a.clearHit()
    curr = a.hitCount
    clearHitMessage = '''<h1>Cur hitCount: {}</h1>'''.format(curr)
    return clearHitMessage

@app.route('/getHit')
def getHit():
    curr = a.hitCount
    getHitMessage = '''<h1>Cur hitCount: {}</h1>'''.format(curr)
    return getHitMessage

@app.route('/clearMiss')
def clearMiss():
    a.clearMiss()
    curr = a.missCount
    clearMissMessage = '''<h1>Cur missCount: {}</h1>'''.format(curr)
    return clearMissMessage

@app.route('/getMiss')
def getMiss():
    curr = a.missCount
    getMissMessage = '''<h1>Cur missCount: {}</h1>'''.format(curr)
    return getMissMessage

@app.route('/example-route')
def example_route():
    def GetImageURL(lat,lng):
        """implement a stub version of GetImageURL() that returns a random number as a string for
        purposes of this problem"""
        return lat*lng
    def checkCoordinates(lat,lng):
        condition1 = (lat >= -90 and lat <= 90)
        condition2 = (lng >= -180 and lng <= 180)
        condition3 = condition2 and condition1
        return condition3
    try:
        lat = float(request.args['lat'])
        lng = float(request.args['lng'])
        if checkCoordinates(lat,lng):
            hashCompute = GetImageURL(lat,lng)
            pageUrl = a.checkCache(hashCompute)
            compute = '''<h1>The Latitude value is: {} & The Longitude value is: {}</h1></h1>
              <h1>The URL string is: {}</h1>'''.format(lat,lng,pageUrl)
            #a.inc("hit")
            return compute
        else:
            #a.inc("miss")
            abort(400)
    except ValueError:
        abort(400)
if __name__ == '__main__':
    #logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    app.run(host='0.0.0.0',port=38080,debug=True)