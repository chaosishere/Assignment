from flask import Flask

def create_crud():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello World!"
    
    return app