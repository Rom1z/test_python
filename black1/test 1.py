def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Error: Unknown operation"

# Примеры использования калькулятора
print(calculator("add", 3, 8))        # Ожидаемый результат: 11
print(calculator("subtract", 10, 5))  # Ожидаемый результат: 5
print(calculator("multiply", 4, 7))   # Ожидаемый результат: 28
print(calculator("divide", 9, 3))     # Ожидаемый результат: 3
print(calculator("divide", 9, 0))     # Ожидаемый результат: "Error: Division by zero"
print(calculator("unknown", 9, 3))    # Ожидаемый результат: "Error: Unknown operation"
