from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecret"
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    if request.json.get('username') == 'admin' and request.json.get('password') == 'pass':
        token = create_access_token(identity=request.json['username'])
        return jsonify(access_token=token)
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({"message": "Protected content!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
