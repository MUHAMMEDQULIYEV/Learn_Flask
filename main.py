from flask import Flask,request,jsonify,render_template


app=Flask(__name__)

Driver={
    14:{"name":"Fernando Alonso","team":"Aston Martin"},
    1:{"name":"Max Verstappen","team":"Red Bull"},
    81:{"name":"Oscar Pastry","team":"Mclaren"}   
}

@app.route("/")
def hello_world():
    return render_template("drivers.html",drivers=Driver)

@app.route("/driver/<int:driver_id>")
def get_driver(driver_id):
    driver=Driver.get(driver_id)
    if not driver:
        return jsonify({"error":"Driver  not found"}),404
    return jsonify(driver)
@app.route("/drivers/add",methods=["POST"])
def add_driver():
    data=request.get_json()
    number=data["number"]
    name=data["name"]
    team=data["team"]
    Driver[number]={"name":name,
                  
                  "team":team}
    return jsonify({"message":"driver message","driver":Driver[number]}),201
    
    
@app.route("/drivers",methods=["GET"])
def return_drivers():
    return jsonify(Driver), 200
    
   



    
    
    
    
    
    
@app.route("/predict",methods=['POST'])
def predict_lap():
    data=request.get_json()
    return jsonify({"predicted_time_s":81.2,"confidence":0.85})
    
    

    


if __name__ == "__main__":
    app.run(debug=True)
    
