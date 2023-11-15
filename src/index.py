from flask import Flask, render_template, request
# Things needed to render the current test to work
# request is essentially a global variable that has any
# values from a request given from the connection.
# Flask is the actual application which is used to run
# render_template builds the website including any
# Jinja code that was used to make templates

port = 3123
TEMPLATE_FOLDER = "templates"



app = Flask(__name__)

@app.route(f"/")
def home():
    return render_template("index.html")

@app.route(f"/test_if", methods=["GET", "POST"])
def test_if_statement():
    if request.method == "POST":
        return render_template("test_if.html", value=request.form["value"])
    return render_template("test_if.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=port, debug=True)