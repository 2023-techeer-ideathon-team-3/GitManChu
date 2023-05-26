from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:23942394@localhost:3306/test'  # MySQL 연결 정보로 대체해야 함
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10))
    address = db.Column(db.String(100))
    age = db.Column(db.Integer)
    friends = db.relationship('Friend', backref='user', lazy=True)


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)


@app.route('/api/friends/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    gender = data.get('gender')
    address = data.get('address')
    age = data.get('age')

    user = User(name=name, gender=gender, address=address, age=age)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})

@app.route('/', methods=['POST'])
def add_friend():
    data = request.json
    name = data.get('name')
    age = data.get('age')

    friend = Friend(name=name, age=age)
    db.session.add(friend)
    db.session.commit()

    return jsonify({'message': 'Friend added successfully'})

@app.route('/<int:friend_id>', methods=['PUT'])
def update_friend(friend_id):
    friend = Friend.query.get_or_404(friend_id)

    data = request.json
    name = data.get('name')
    age = data.get('age')

    friend.name = name
    friend.age = age
    db.session.commit()

    return jsonify({'message': 'Friend updated successfully'})

@app.route('/<int:friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    friend = Friend.query.get_or_404(friend_id)
    db.session.delete(friend)
    db.session.commit()

    return jsonify({'message': 'Friend deleted successfully'})


if __name__ == '__main__':
    app.run()
