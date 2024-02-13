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
        print ("Database initializing...")
        conn = psycopg2.connect(database="app_db", host="pg_db", user="app_user", password="securePass123!", port="5432")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE courses(
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR (50) UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic VARCHAR (20) NOT NULL);
            """)
        print ("Database initialized successfully")
        conn.commit

        print ("Inserting data into table courses")
        cursor.execute("INSERT INTO courses(course_name, course_instructor, topic) VALUES('Linux System Administration','Marcin Kujawski','Linux');");
        cursor.execute("INSERT INTO courses(course_name, course_instructor, topic) VALUES('Kubernetes Administration','Marcin Kujawski','Kubernetes');");
        cursor.execute("INSERT INTO courses(course_name, course_instructor, topic) VALUES('Linux for System Engineers','Marcin Kujawski','Linux');");
        conn.commit
        print ("Data inserted into DB table")

        print ("Getting database content...")
        dbContent = []
        cursor.execute('SELECT * FROM courses;')
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('init.html', data='Database successfully initialized')
    except:
        return render_template('init.html', data='Database already exist, doing nothing')

@app.route('/db_get')
def db_get():
    try:
        conn = psycopg2.connect(database="app_db", host="pg_db", user="app_user", password="securePass123!", port="5432")
        cursor = conn.cursor()
        dbContent = []
        cursor.execute('SELECT * FROM courses;')
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('get.html', data=rows)

    except:
        return render_template('init.html', data='Database is not yet initialized, please navigate to Application -> Init')

@app.route('/db_add')
def db_add():
    return render_template('add.html')

@app.route('/db_add', methods=['POST'])
def db_add_post():
    course = request.form['course']
    trainer = request.form['trainer']
    category = request.form['category']

    try:
        conn = psycopg2.connect(database="app_db", host="pg_db", user="app_user", password="securePass123!", port="5432")
        conn.autocommit = True
        cursor = conn.cursor()
        
        insert_query = ''' INSERT INTO courses(course_name, course_instructor, topic) VALUES (%s,%s,%s);'''
        record = (course, trainer, category)
        cursor.execute(insert_query, record)
        print("INSERT INTO courses(course_name, course_instructor, topic) VALUES('" + course + "','" + trainer + "','" + category  + "');")
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")
        
        cursor.close()
        conn.close()

        return render_template('init.html', data='New course ' + course + ' (trainer: ' + trainer  + ') in category ' + category + ' was added to database.')

    except:
        return render_template('init.html', data='An error occurred when adding new course.')

@app.route('/db_remove')
def db_remove():
    return render_template('remove.html')

@app.route('/db_remove', methods=['POST'])
def db_remove_post():
    course_id = request.form['course_to_delete']

    try:
        conn = psycopg2.connect(database="app_db", host="pg_db", user="app_user", password="securePass123!", port="5432")
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute('DELETE FROM courses WHERE course_id = ' + course_id + ';')

        cursor.close()
        conn.close()
        
        return render_template('init.html', data='Course with id' + course_id + ' was deleted from database.')

    except:
        return render_template('init.html', data='An error occurred when deleting the course.')
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
