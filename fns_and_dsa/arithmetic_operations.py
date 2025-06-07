def perform_operation(num1: float, num2: float, operation: str):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            # Change this line to match the expected error message
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        # Handle invalid operations
        # You might also want to change this to match a specific expected message if the checker is strict here too
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
