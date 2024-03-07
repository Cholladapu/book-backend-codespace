from flask import Flask, jsonify

app = Flask(__name__)

books=[
    {"id":1,"title":"Book 1","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"}
]
@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

@app.route("/books",methods=["GET"])
def get_all_books():
    return jsonify({"books":books})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)