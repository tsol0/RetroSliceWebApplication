from config import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer)
    arcade_score = db.Column(db.Integer, nullable=False)
    bowling_score = db.Column(db.Integer, nullable=False)
    pizzas_consumed = db.Column(db.Integer, nullable=False)
    slushy_preference = db.Column(db.String(60), unique=False, nullable=False)
    slushies_consumed = db.Column(db.Integer, nullable=False)
    employed = db.Column(db.Boolean, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "arcadeScore": self.arcade_score,
            "bowlingScore": self.bowling_score,
            "pizzasConsumed": self.pizzas_consumed,
            "slushyPreference": self.slushy_preference,
            "slushiesConsumed"
            "employed": self.employed,
            "email": self.email
        }
