from flask import url_for,render_template
from app import app
from flask_googlemaps import GoogleMaps

@app.route('/')
def index():
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)

