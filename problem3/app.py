from flask import Flask
from flask import request
from flask import abort
app = Flask(__name__)


@app.route('/')
def info():
    _info = '''
    <h1>Sample for Application Endpoint is :- http://127.0.0.1:5000/example-route?lat=90&lng=180</h1>
    <h2>-90 >= lat <=90 </h2>
    <h2>-180 >= lat <=180 </h2>
    '''
    return _info

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
            return compute
        else:
            abort(400)
    except ValueError:
        abort(400)
if __name__ == '__main__':
    app.run()