# Backend for the app in Flask

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from the backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

"""
After creating app.py and auth.py, run these bash commands to containerize and push to AWS ECR:


aws ecr create-repository --repository-name auth-service
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

# Build and push Docker image
docker build -t auth-service .
docker tag auth-service:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/auth-service
docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/auth-service

"""
