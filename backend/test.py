from flask import Flask
from routes import friends_bp

app = Flask(__name__)
app.register_blueprint(friends_bp)

if __name__ == '__main__':
    app.run()