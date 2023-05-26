from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0000@localhost:3306/test'  # MySQL 연결 정보로 대체해야 함
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

if __name__ == '__main__':
    app.run(debug=True)
