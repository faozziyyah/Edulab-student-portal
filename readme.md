# Edulab-student-portal

full stack CRUD web application built with HTML, CSS, Bootstrap, JavaScript, Python, Postgres, and Flask framework. <br />
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Screenshot](#screenshot)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Useful resources](#useful-resources)
- [To use](#usage)

## Overview

### The challenge

Users should be able to:

- Add a new student.
- View each student's details.
- Delete a student data.
- View the optimal layout for the site depending on their device's screen size

### Screenshot

![](static/images/screenshot.png)
![](static/images/screenshot1.png)
![](static/images/screenshot2.png)


### Links

- Solution URL: (https://github.com/faozziyyah/Edulab-student-portal)
- Live link: (https://edulab-student-portal.herokuapp.com/)

## My process

### Built with

- HTML
- CSS
- Bootstrap
- Javascript
- Ajax
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - A web development microframework built with python
- Postgres

### What I learned

- How to connect to a database
- How to use the Jinja template

```js
$( window ).on("load", function() {
    $("#myModal").modal("show");
    $("#content").hide();
    $(".update-content").hide();
    $(".edit-word, .edit-meaning").hide();
    $(".submit, .cancel").hide();
}
```

```Python
@app.route('/delete/<string:id_data>', methods =['GET'])
def delete(id_data):
    flash('student record deleted successfully')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(' delete from students where student_id=%s', (id_data))
    conn.commit()
    return redirect(url_for('students'))
```

```HTML
{% for student in students %}
<tr>
    <td>{{ student['student_id'] }}</td>
    <td class="word-word">{{ student['firstname'] }} {{ student['lastname'] }}</td>
    <td class="word-meaning">{{ student['gender'] }}</td>
    <td class="word-meaning">{{ student['jambscore'] }}</td>
    <td class="word-meaning">{{ student['email'] }}</td>
</tr>
```

### Useful resources

- [Flask](https://flask.palletsprojects.com/en/2.1.x/) - A web development microframework built with python
<<<<<<< HEAD
- [Postgresql](https://www.postgresql.org/) - The world's most popular open source database
=======
- [MySQL](https://www.mysql.com/) - The world's most popular open source database
>>>>>>> 8a9870f67ee869db39a066d9324ea5c44c0a0b47
