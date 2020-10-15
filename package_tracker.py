from flask import Flask, render_template
from config import Config
from map.map import map
from app.shipping_form import ShippingForm
from config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    return "Package Tracker"


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    sf = ShippingForm()
    return render_template('shipping_request.html', sf=sf)
