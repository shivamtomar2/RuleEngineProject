# Rule Engine Project

## Overview
This project is a simple rule engine built using Flask and MongoDB. It allows users to create and evaluate rules based on specific conditions using logical operators such as AND and OR.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Non-Functional Requirements](#non-functional-requirements)
- [Contributing](#contributing)

## Prerequisites
- Python 3.x
- Flask
- pymongo
- MongoDB installed locally or a cloud instance.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shivamtomar2/RuleEngineProject.git
Navigate to the project directory:
--cd RuleEngineProject

Create a virtual environment (optional but recommended):
--python -m venv env
--source env/bin/activate  # For Mac/Linux

Install the required packages:
--pip install -r requirements.txt

Usage
Start the MongoDB server if it’s not already running:
--mongod

Run the Flask application:
--python app.py

The application will be running at http://127.0.0.1:5000.

API Endpoints
A) 
Create Rule
-Endpoint: /create_rule
-Method: POST
Request Body:
    json
    {
        "rule_id": "1",
        "type": "AND",
        "left": {"type": "operand", "value": "age > 30"},
        "right": {
            "type": "OR",
            "left": {"type": "operand", "value": "department == \"Sales\""},
            "right": {"type": "operand", "value": "salary > 50000"}
        }
    }
Response:
    json
    {
        "message": "Rule created",
        "rule": { ... }
    }
B) 
Evaluate Rule
-Endpoint: /evaluate_rule
-Method: POST
Request Body:
    json
    {
        "ast": { ... },  // The AST structure you get from the create_rule response
        "data": { "age": 35, "department": "Sales", "salary": 60000 }
    }
Response:
    json
    
    {
        "result": true
    }
Non-Functional Requirements
Security: Implemented basic input validation to prevent injection attacks.
Performance: Efficient query handling through indexed MongoDB collections.

Contributing
If you'd like to contribute, please fork the repository and submit a pull request.

