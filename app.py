from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # return "<p>This is the HOME page!</p>"
    # API CALL  --> title_variable ????
    return render_template("index.html", title_variable="hello")

@app.route("/about")
def about():
    return render_template("about.html")
    # return "<p>This is the ABOUT page!</p>"

@app.route("/courses")
def courses():
    return render_template("courses.html")
    # return "<p>This is the COURSES page!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)