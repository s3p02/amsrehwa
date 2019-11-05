from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def info():
    return "Sample for Application Endpoint is :- http://127.0.0.1:5000/example-route?lat=90&lng=180"

@app.route('/example-route')
def example_route():
    lat = request.args['lat']
    lng = request.args['lng']
    compute = '''<h1>The Latitude value is: {}</h1>
              <h1>The Longitude value is: {}</h1>'''.format(lat,lng)
    return compute

if __name__ == '__main__':
    app.run()