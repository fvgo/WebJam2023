from flask import Flask, render_template, request
import src.forms

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
    form.validate_on_submit()
    print(form.errors)
    print(request.values)
    return render_template("courses.html", form=form, request=request)
    # return "<p>This is the COURSES page!</p>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)