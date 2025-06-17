from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Configure DynamoDB connection
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('your_table_name')

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    table.put_item(Item=data)
    return jsonify({'message': 'Item added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
