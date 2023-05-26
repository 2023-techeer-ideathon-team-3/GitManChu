from flask import Flask

app = Flask(__name__)


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:23942394@localhost:3306/test'  # MySQL 연결 정보로 대체해야 함
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    gitAddress = db.Column(db.String(100))


    friends = db.relationship('Friend', backref='user', lazy=True)


@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    gitAddress = data.get('gitAddress')


    user = User(name=name, gitAddress=gitAddress)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})


@app.route('/api/updateUser', methods=['POST'])
def update_user():
    data = request.json
    user_id = data.get('user_id')
    name = data.get('name')
    gitAddress = data.get('gitAddress')

    # 해당 user_id의 사용자 존재 여부 확인
    user = User.query.get_or_404(user_id)

    # 사용자 정보 업데이트
    user.name = name
    user.gitAddress = gitAddress

    db.session.commit()

    return jsonify({'message': 'User updated successfully'})

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'name': user.name,
            'gitAddress': user.gitAddress,
        })
    return jsonify(user_list)


    friend = Friend.query.get_or_404(friend_id)

    data = request.json@app.route('/users/<int:user_id>/friends', methods=['POST'])
def add_friend(user_id):
    # 유저 존재 여부 확인
    user = User.query.get_or_404(user_id)

    # 요청 데이터에서 친구 이름과 나이 가져오기
    data = request.json
    user_id = data.get('user_id')

    # 친구 생성 및 연결
    friend = Friend(user_id=user_id)
    db.session.add(friend)
    db.session.commit()

    return jsonify({'message': 'Friend added successfully'})
@app.route('/users/<int:user_id>/friends', methods=['GET'])
def get_friends(user_id):
    user = User.query.get_or_404(user_id)

    friends = Friend.query.join(User).filter(User.id == user_id).all()
    friend_data = [{'friend_name': friend.name, 'user_name': user.name, 'user_age': user.age} for friend in friends]

    return jsonify(friend_data)

@app.route('/<int:friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    friend = Friend.query.get_or_404(friend_id)
    db.session.delete(friend)
    db.session.commit()

    return jsonify({'message': 'Friend deleted successfully'})

if __name__ == '__main__':
    app.run()