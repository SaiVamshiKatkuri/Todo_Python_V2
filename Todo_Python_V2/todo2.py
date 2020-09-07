from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Blueprint, Flask, jsonify, request
from flask_classful import FlaskView, route
import json


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/test1'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), nullable=False)  
       
@app.route('/',methods=['GET'])
def hello():
     return "Hello From Server!"
    
@app.route('/addtodo/<todo>')
def addtodo(todo):
    newTodo =Todo(todo = todo)
    db.session.add(newTodo)
    db.session.commit()
    return "SUCCESS"

@app.route('/gettodos/')
def gettodos():
    todos=Todo.query.all()
    todo_array=[]
    for t in todos:
        todo_array.append([t.todo,t.id])
    print(todo_array)
    return json.dumps(todo_array) 
@app.route('/newtodos/')
def newtodos():
     todos=Todo.query.delete()

@app.route('/deletetodos/<id>')
def deletetodos(id):
     i=id
     Todo.query.filter_by(id=i).delete()


db.create_all()
app.run(port="3000")