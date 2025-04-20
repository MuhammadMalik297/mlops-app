from flask import Flask, jsonify, request
from flask_cors import CORS
from auth import auth_bp
from utils import decode_token

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'Missing token'}), 403
    token = auth_header.split(" ")[1]
    try:
        user_data = decode_token(token)
        return jsonify({'message': f'Welcome user {user_data["user_id"]}'}), 200
    except Exception as e:
        return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
