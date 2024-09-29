from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from routes.auth import auth_bp
from routes.ops import ops_bp
from routes.client import client_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(ops_bp, url_prefix="/ops")
app.register_blueprint(client_bp, url_prefix="/client")

# Error Handling
@app.errorhandler(Exception)
def handle_exception(e):
    response = {
        "error": str(e),
        "message": "An unexpected error occurred"
    }
    return jsonify(response), 500

if __name__ == "__main__":
    app.run(debug=True)
