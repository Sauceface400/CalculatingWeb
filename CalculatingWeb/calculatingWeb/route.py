import os
from flask import redirect, url_for, render_template
from calculatingWeb import app, db
from calculatingWeb.model import USDconverter, taxes
from calculatingWeb.form import currency_convert, taxCalculate

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/currency", methods=['GET', 'POST'])
def currency():
    form = currency_convert()
    if form.validate_on_submit():
        ringgit = USDconverter(amount=form.amount.data)
        db.session.add(ringgit)
        db.session.commit()
    total = USDconverter.query.all()
    return render_template('currency.html', form=form, total=total)

@app.route("/tax", methods=['GET', 'POST'])
def tax():
    form = taxCalculate()
    if form.validate_on_submit():
        taxGST = taxes(amount=form.amount.data)
        db.session.add(taxGST)
        db.session.commit()
    total = taxes.query.all()
    return render_template('taxes.html', form=form, total=total)

@app.route("/delete1", methods=['GET', 'POST'])
def deletedataUSD():
    USDconverter.query.delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/delete2", methods=['GET', 'POST'])
def deletedataTax():
    taxes.query.delete()
    db.session.commit()
    return redirect(url_for('home'))
