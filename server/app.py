
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
     # Print the parameter to the terminal
    print(f"{parameter}")

    # Return the parameter as a response to display it in the web browser
    return f'hello'
    
@app.route('/count/<int:parameter>')
def count(parameter):
    
    # Generate a list of numbers in range of paramter 
    numbers = list(range(parameter + 1))
    
    # format the numbers as seperate lines 
    numbers_text = '\n'.join([str(number) for number in numbers])
    
    # return the formatted list of numbers as a response 
    return f'{numbers_text}'

@app.route ('/math/<int:parameter1>/<string:operation>/<int:parameter2>')
def math(parameter1, operation, parameter2):
    # Check if the operation is addition
    if operation == '+':
        result = parameter1 + parameter2
    # Perform other math operations based on the operation parameter
    elif operation == 'add':
        result = parameter1 + parameter2
    elif operation == '-':
        result = parameter1 - parameter2
    elif operation == 'subtract':
        result = parameter1 - parameter2
    elif operation == '*':
        result = parameter1 * parameter2
    elif operation == 'multiply':
        result = parameter1 * parameter2
    elif operation == '/':
        result = parameter1 / parameter2
    elif operation == 'div':
        result = parameter1 / parameter2
    elif operation == '%':
        result = parameter1 % parameter2
    elif operation == 'mod':
        result = parameter1 % parameter2
    else:
        return 'Invalid operation'
    
    # Convert the result to a string
    result_str = str(result)
    
    # Return the result as a response
    return result_str
if __name__ == '__main__':
    app.run(port=5555, debug=True)



 