from flask import Flask, render_template
from config import Config
from map.map import map
from app.shipping_form import ShippingForm
from flask_migrate import Migrate
from app.models import (
    db, Package
)

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    packages = Package.query.all()
    return render_template('package_status.html')


@app.route("/new_package", methods=["GET", "POST"])
def new_package():
    sf = ShippingForm()
    sf.origin.choices = [(city, city) for city in map]
    sf.destination.choices = [(city, city) for city in map]
    if sf.validate_on_submit():
        data = sf.data
        new_package = Package(sender=data["sender_name"],
                              recipient=data["recipient_name"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect(url_for('.index'))
    return render_template('shipping_request.html', sf=sf)
