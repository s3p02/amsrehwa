from flask import Flask
app = Flask(__name__)


@app.route('/')
def info():
    return "Application Endpoint is :- http://127.0.0.1:5000/LatitudeValue/LongitudeValue"

@app.route('/<lat>/<lng>')
def latLongPairs(lat,lng):
    return "Hello!\nLAT:{}\nLNG:{}".format(lat,lng)

if __name__ == '__main__':
    app.run()