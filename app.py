from flask import Flask, render_template, request
import src.forms
import requests
from api import main

app = Flask(__name__)

app.config["SECRET_KEY"] = "HASHVALUE"


@app.route("/")
def home():
    # return "<p>This is the HOME page!</p>"
    # API CALL  --> title_variable ????
    # return render_template("index.html", title_variable="hello")
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
    # return "<p>This is the ABOUT page!</p>"

@app.route("/courses", methods=["GET", "POST"])

def courses():
    form = src.forms.ClassForm()
    # if form.validate_on_submit():
    #     render_template("courses.html", form=form)
    user_course = "__________"
    difficulty_average = "__________"
    user_dept = request.values.get("dept_selected")
    user_class_number = request.values.get("class_number")
    url = f"https://api-next.peterportal.org/v1/rest/courses?department={user_dept}&courseNumber={user_class_number}"
    error = ""
    if form.validate_on_submit():
        response = requests.get(url).json()
        if response["payload"]:
            user_dept = response["payload"][0]["department"]
            user_class_number = response["payload"][0]["courseNumber"]
            user_course = response["payload"][0]["id"]
            difficulty_average = main.find_difficulty_average(user_course)
        else:
            error = "Class could not be found."
    return render_template(
        "courses.html",
        form=form,
        request=request,
        entered_course=user_course,
        course_returned=difficulty_average,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
