from flask import Flask
from flask import request
from flask import abort
import logging
import sys
app = Flask(__name__)

class lruCache:
    __cacheSize = 3#000
    hitCount = 0
    missCount = 0
    def __init__(self):
        print("LRU CACHE")

    def inc(self,option):
        if option == "hit":
            prev = self.hitCount
            print("CLASS lruCache:inc:incHit,prev: {}".format(prev))
            self.hitCount += 1
            curr = self.hitCount
            print("CLASS lruCache:inc:incHit,curr: {}".format(curr))
        elif option == "miss":
            prev = self.missCount
            print("CLASS lruCache:inc:incMiss,prev: {}".format(prev))
            self.missCount += 1
            curr = self.missCount
            print("CLASS lruCache:inc:incMiss,curr: {}".format(curr))
    
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
    <h1>Sample for Application Endpoint is :- http://127.0.0.1:5000/example-route?lat=90&lng=180</h1>
    <h2>-90 >= lat <=90 </h2>
    <h2>-180 >= lat <=180 </h2>
    '''
    return _info


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
    clearMissMessage = '''<h1>Cur clearMiss: {}</h1>'''.format(curr)
    return clearMissMessage

@app.route('/getMiss')
def getMiss():
    curr = a.missCount
    getMissMessage = '''<h1>Cur missCount: {}</h1>'''.format(curr)
    return getMissMessage

@app.route('/example-route')
def example_route():
    def checkCoordinates(lat,lng):
        condition1 = (lat >= -90 and lat <= 90)
        condition2 = (lng >= -180 and lng <= 180)
        condition3 = condition2 and condition1
        return condition3
    try:
        lat = float(request.args['lat'])
        lng = float(request.args['lng'])
        if checkCoordinates(lat,lng):
            compute = '''<h1>The Latitude value is: {}</h1>
              <h1>The Longitude value is: {}</h1>'''.format(lat,lng)
            a.inc("hit")
            return compute
        else:
            a.inc("miss")
            abort(400)
    except ValueError:
        abort(400)
if __name__ == '__main__':
    #logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    app.run()