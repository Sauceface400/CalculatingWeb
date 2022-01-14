from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired

class currency_convert(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    multiply = SubmitField('Convert to MYR')
    divide = SubmitField('D')

class taxCalculate(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired()])
    send = SubmitField('Send')