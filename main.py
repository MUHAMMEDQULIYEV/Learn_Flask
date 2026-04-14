from flask import Flask,request,jsonify


app=Flask(__name__)

Driver={
    14:{"name":"Fernando Alonso","team":"Aston Martin"},
    1:{"name":"Max Verstappen","team":"Red Bull"},
    81:{"name":"Oscar Pastry","team":"Mclaren"}   
}

@app.route("/")
def hello_world():
    return "<p>Hello New Flask App</p>"

@app.route("/driver/<int:driver_id>")
def get_driver(driver_id):
    driver=Driver.get(driver_id)
    if not driver:
        return jsonify({"error":"Driver  not found"}),404
    return jsonify(driver)
    
    
@app.route("/predict",methods=['POST'])
def predict_lap():
    data=request.get_json()
    return jsonify({"predicted_time_s":81.2,"confidence":0.85})
    
    

    


if __name__ == "__main__":
    app.run(debug=True)
    
