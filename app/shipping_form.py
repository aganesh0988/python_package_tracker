from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField, BooleanField


class ShippingForm(FlaskForm):
    sender_name = StringField("Sender name", [DataRequired()])
    recipient_name = StringField("Recipient name", [DataRequired()])
    origin = StringField("Origin", [DataRequired()])
    destination = StringField("Destination", [DataRequired()])
    express_shipping_desired = BooleanField("Express Shipping Desired")
    submit = SubmitField("Submit")
    cancel = SubmitField("Cancel")
