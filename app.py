from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client['rule_engine_db']
rules_collection = db['rules']

# AST Node Class
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # 'operator' or 'operand'
        self.left = left
        self.right = right
        self.value = value

# API to create a rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_data = request.json
    rule_ast = Node(type=rule_data['type'], left=rule_data['left'], right=rule_data['right'])
    rule = {
        "rule_id": rule_data['rule_id'],
        "ast": rule_ast.__dict__
    }
    rules_collection.insert_one(rule)
    return jsonify({"message": "Rule created", "rule": rule_ast.__dict__})

# Function to evaluate AST
def evaluate_rule(ast, data):
    if ast['type'] == 'AND':
        return evaluate_rule(ast['left'], data) and evaluate_rule(ast['right'], data)
    elif ast['type'] == 'OR':
        return evaluate_rule(ast['left'], data) or evaluate_rule(ast['right'], data)
    elif ast['type'] == 'operand':
        return eval(ast['value'], data)

# API to evaluate a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate():
    ast = request.json['ast']
    data = request.json['data']
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
