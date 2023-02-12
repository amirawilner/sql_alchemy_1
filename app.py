
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Student {}>'.format(self.name)

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/student/new', methods=['GET', 'POST'])
def new_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        
        student = Student(name=name, age=age, grade=grade)
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    return render_template('new_student.html')

@app.route('/student/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
      
        db.session.commit()
        return redirect('/')
    return render_template('edit_student.html', student=student)

@app.route('/student/<int:id>/delete', methods=['GET', 'POST'])
def delete_student(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect('/')
    return render_template('delete_student.html', student=student)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
