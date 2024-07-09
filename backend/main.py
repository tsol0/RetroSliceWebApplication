from flask import request, jsonify
from config import app, db
from models import Customer

@app.route("/customers", methods=["GET"])
def get_customers(): 
    customers = Customer.query.all()
    json_customers = list(map(lambda y:y.to_json(), customers))
    return jsonify({"customers": json_customers})

@app.route("/create_customer", methods=["POST"])
def create_customer():
    name = request.json.get("name")
    age = request.json.get("age")
    arcade_score = request.json.get("arcadeScore")
    bowling_score = request.json.get("bowlingScore")
    pizzas_consumed = request.json.get("pizzasConsumed")
    slushy_preference = request.json.get("slushyPreference")
    slushies_consumed = request.json.get("slushiesConsumed")
    employed = request.json.get("employed")
    email = request.json.get("email")
    
    if not name or not age or not arcade_score or not bowling_score or not pizzas_consumed or not slushy_preference or not slushies_consumed or not employed or not email:
        return (
            jsonify({"message": "Invalid information was inputed"}),400,
        )
        
    new_customer = Customer(name= name, age= age, 
                            arcade_score= arcade_score, bowling_score= bowling_score,
                            pizzas_consumed= pizzas_consumed, slushy_preference=slushy_preference,
                            slushies_consumed= slushies_consumed,
                            employed= employed, email= email)
    
    try:
        db.sessioin.add(new_customer)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

