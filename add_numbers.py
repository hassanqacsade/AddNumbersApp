def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    print(add_numbers(3, 5))  # Expected Output: 8
    print(subtract_numbers(5, 3))  # Expected Output: 2
    print(multiply_numbers(2, 3))  # Expected Output: 6
    print(divide_numbers(6, 3))  # Expected Output: 2.0
