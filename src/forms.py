from flask_wtf import FlaskForm
from flask import render_template
import wtforms
import wtforms.validators


class ClassForm(FlaskForm):
    @staticmethod
    def dept_abbrev_pair():
        import json
        with open("static/department_abbrev_pair.json") as file:
            return json.load(file)

    dept_selected = wtforms.SelectField(label="departments", \
                                     choices=dept_abbrev_pair(),
                                     validators=[wtforms.validators.InputRequired(message="Please select a department."), wtforms.validators.NoneOf(("ALL", ""))])
    class_number = wtforms.StringField(label="class_number", validators=[wtforms.validators.length(1, message="Please enter a class number.")])
    submit = wtforms.SubmitField(label="submit")