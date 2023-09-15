from flask import Flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
CORS(app)

class Person(db.Model):
     __tablename__ = 'persons'
     id = db.Column(db.Integer, primary_key=True)
     first_name = db.Column(db.String(100), nullable=False)
     last_name = db.Column(db.String(100), nullable=False)

     def __init__(self, first_name, last_name):
          self.first_name = first_name
          self.last_name = last_name

# API Routes
@app.route('/')
def index():
    return '<h1>Hello Welcome</h1>'

@app.route('/persons', methods = ['GET'])
def get_all_persons():
    persons = Person.query.all()
    result = []
    for person in persons:
        result.append({'first_name': person.first_name, 'last_name': person.last_name})
    return jsonify(result)

@app.route('/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person:
        return jsonify({'id': person.id, 'first_name': person.first_name, 'last_name': person.last_name})
    else:
        return jsonify({'error': 'Person not found'})

@app.route('/persons/<first_name>,<last_name>', methods=['GET'])
def get_person_by_name(first_name, last_name):
    person = Person.query.filter_by(first_name=first_name, last_name=last_name).first()
    if person:
        return jsonify({'id': person.id, 'first_name': person.first_name, 'last_name': person.last_name})
    else:
        return jsonify({'error': 'Person not found'})

@app.route('/persons', methods=['POST'])
def create_person():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    person = Person(first_name, last_name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'})

@app.route('/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get(person_id)
    if person:
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        person.first_name = first_name
        person.last_name = last_name
        db.session.commit()
        return jsonify({'message': 'Person updated successfully'})
    else:
        return jsonify({'error': 'Person not found'})

@app.route('/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person deleted successfully'})
    else:
        return jsonify({'error': 'Person not found'})

if __name__ == '__main__':
    #db.create_all()
    app.run(host="0.0.0.0",port="5000",debug=True)
