import psycopg2
import subprocess
import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html', data='This is a test message in test page')

@app.route('/db_init')
def db_init():
    try:
        return render_template('init.html', data='Database successfully initialized')
    except:
        return render_template('init.html', data='Database already exist, doing nothing')

@app.route('/db_get')
def db_get():
    try:
        return render_template('get.html', data=rows)
    except:
        return render_template('init.html', data='Database is not yet initialized, please navigate to Application -> Init')

@app.route('/db_add')
def db_add():
    return render_template('add.html')

@app.route('/db_add', methods=['POST'])
def db_add_post():
    try:
        return render_template('init.html', data='New course ' + course + ' (trainer: ' + trainer  + ') in category ' + category + ' was added to database.')
    except:
        return render_template('init.html', data='An error occurred when adding new course.')

@app.route('/db_remove')
def db_remove():
    return render_template('remove.html')

@app.route('/db_remove', methods=['POST'])
def db_remove_post():
    try:
        return render_template('init.html', data='Course with id' + course_id + ' was deleted from database.')
    except:
        return render_template('init.html', data='An error occurred when deleting the course.')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
