from ast import Return
import os
from flask import Flask, render_template, request, redirect, url_for, flash, redirect, current_app
#from flaskext.mysql import MySQL
#import pymysql.cursors
import datetime, json, psycopg2

app = Flask(__name__)

app.secret_key = 'secret'
def get_db_connection():
  conn = psycopg2.connect("dbname=portal user=postgres password=opeyemi2001 host=localhost")
  return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from students')
    rv = cur.fetchall()
    for item in rv:
        print(item)
    cur.close()

    return render_template('students.html', students=rv)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        name= ''
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        jambscore = request.form['jambscore']
        email = request.form['email']
        student_id = request.form['student_id']
        nextofkin = request.form['nextofkin']
        dateofbirth = request.form['dateofbirth']
        address = request.form['address']
        gender = request.form['gender']
        stateoforigin = request.form['stateoforigin']
        localgovernment = request.form['localgovernment']
        image = request.files['image']

        if firstname and lastname and email and student_id and dateofbirth and gender and phone and address and stateoforigin and localgovernment and jambscore and nextofkin and image:
            name = firstname + '_' + lastname + '_' + image.filename
            filepath = os.path.join(current_app.root_path, 'static/images/' + name)
            image.save(filepath)
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('insert into students(student_id, firstname, lastname, phone, jambscore, email, nextofkin, dateofbirth, address, gender, stateoforigin, localgovernment, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (student_id, firstname, lastname, phone, jambscore, email, nextofkin, dateofbirth, address, gender, stateoforigin, localgovernment, name))
            conn.commit()
            cur.close()
            print(image)
        else:
            flash('Please fill all fields', 'flash_error')  
            return redirect(url_for('students'))      
        flash('student successfully added!')
    return redirect(url_for('students'))

@app.route('/details', methods =['GET', 'POST'])
def details():
    student = ''
    detail = request.form['id']
    if request.method == 'POST':
      conn = get_db_connection()
      cur = conn.cursor()
      cur.execute('select * from students where student_id=%s', (detail))
      rv = cur.fetchall()
      student = rv
      #for item in rv:
        #print(item)
      #cur.close()
    #return redirect(url_for('details'))
      return render_template('details.html', student = student)

@app.route('/delete/<string:id_data>', methods =['GET'])
def delete(id_data):
    flash('student record deleted successfully')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(' delete from students where student_id=%s', (id_data))
    conn.commit()
    return redirect(url_for('students'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        students = ''
        name = request.form.get('searchName') or None
        email = request.form.get('searchEmail') or None
        gender = request.form.get('searchGender') or None
        jamb = request.form.get('searchJamb') or None
        print('jamb:', jamb)

        if name or email or gender or jamb:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('select * from students where firstname like %s or firstname is null or lastname like %s or lastname is null or email like %s or email is null or gender like %s or gender is null or jambscore = %s or jambscore is null order by student_id', (name, name, email, gender, jamb))
            rv = cur.fetchall()
            students = rv
        else:
            flash('Please add a search term', 'flash_success')
            return redirect(url_for('students'))
        flash('Search completed', 'flash_success')
        return render_template('students.html', students = students)
    return redirect(url_for('students'))


if __name__ == '__main__':
    app.run(debug=True)