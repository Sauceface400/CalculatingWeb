from calculatingWeb import db

class USDconverter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Amount('{self.amount}')"

class taxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Amount('{self.amount}')"