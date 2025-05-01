from flask import Flask
from comparar import app as comparar_app

app = Flask(__name__)
app.register_blueprint(comparar_app)

if __name__ == '__main__':
    app.run()