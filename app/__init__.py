from flask import Flask
from flask_googlemaps import GoogleMaps
app = Flask(__name__)


# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBh_x5Sp_GwTwaB9mYEgxJ-oh7d-7JL3Zg"

# Initialize the extension
GoogleMaps(app)

from app import routes