def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first number.
    - num2 (float): The second number.
    - operation (str): The operation to perform. Valid options: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - float or str: The result of the arithmetic operation, or an error message for invalid input or division by zero.
    """

    # Check the operation type and perform corresponding calculation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        # Handle invalid operations
        return "Error: Invalid operation"
