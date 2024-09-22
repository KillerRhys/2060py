""" Todo Web Application
    Coded by TechGYQ
    www.mythosworks.com
    OC:2024.08.01(1000) """

# Imports
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from logic import Logic, TodoItem
import sys
from cli import run_cli

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
        brain.add_item(task)
        return redirect(url_for('index'))
    tasks = brain.show_items()
    return render_template('index.html', form=form, tasks=tasks)


@app.route("/edit/<int:task_id>", methods=['GET', 'POST'])
def edit_task(task_id):
    task_to_edit = brain.session.query(TodoItem).get(task_id)
    form = TodoForm(obj=task_to_edit)

    if form.validate_on_submit():
        new_task_name = form.task.data
        brain.edit_item(task_id, new_task_name)
        return redirect(url_for('index'))

    return render_template('edit.html', form=form, task_id=task_id)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    brain.delete_item(task_id)
    return redirect(url_for('index'))


def run_flask():
    app.run(debug=True)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli()
    else:
        run_flask()
