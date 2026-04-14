from flask import Flask


app=Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>Hello New Flask App</p>"

def main():
    print("Hello from learn-flask!")
    app.run(debug=True)


if __name__ == "__main__":
    main()
