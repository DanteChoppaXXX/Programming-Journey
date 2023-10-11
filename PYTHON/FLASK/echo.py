from flask import Flask, request

app = Flask(import_name=__name__)

@app.route("/echo", methods=["POST"])
def echo():

    name = request.form.get("name", "")
    age = request.form.get("age", "")

    response = "Hey There {}! You said you are {} years old.".format(name, age)

    return response

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=334)