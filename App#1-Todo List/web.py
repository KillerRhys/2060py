""" Todo Web Application
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.08.01(1000) """

# Imports
from logic import Logic
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for WTForms
brain = Logic()


# Form
class TodoForm(FlaskForm):
    task = StringField('Task Name:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        task = form.task.data
        brain.add_task(task)
        return redirect(url_for('index'))
    tasks = brain.get_tasks()
    return render_template('index.html', form=form, tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    brain.delete_task(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
