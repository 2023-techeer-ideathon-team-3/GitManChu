from flask import Flask

app = Flask(__name__)


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0000@localhost:3306/test'  # MySQL 연결 정보로 대체해야 함
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

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)


@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    post_list = []
    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content
        }
        post_list.append(post_data)
    return jsonify(post_list)


@app.route('/posts', methods=['POST'])
def add_post():
        data = request.json
        title = data.get('title')
        content = data.get('content')

        if title and content:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()

            return jsonify({'message': '게시글이 추가되었습니다.'}), 201
        else:
            return jsonify({'error': 'title 또는 content가 누락되었습니다.'}), 400

from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)


app.secret_key = 'myscretkey'
#configuraciones de oauth
oauth = OAuth(app)
github = oauth.register(
    name='github',
    client_id='e4cf94d8a14d851411a7',
    client_secret='81a00d25b89171de7303809cc53077b19070c6f3',
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)
@app.route('/login')
def registro():
   github = oauth.create_client('github')
   redirect_uri = url_for('authorize', _external=True)
   return github.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
   github = oauth.create_client('github')
   token = github.authorize_access_token()
   resp = github.get('user', token=token)
   profile = resp.json()
   # do something with the token and profile
   print(profile, token)
   return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)