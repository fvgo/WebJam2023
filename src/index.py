from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # return "<p>This is the HOME page!</p>"
    return render_template("home.html")

@app.route("/about")
def about():
    return "<p>This is the ABOUT page!</p>"

if __name__ == "__main__":
    app.run(debug=True)