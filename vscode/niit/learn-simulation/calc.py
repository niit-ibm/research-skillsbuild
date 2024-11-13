def perform_operation(x, y, op):
    if op == 'add':
        return x + y
    else:
        return "Invalid operation"

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
op = input("Enter the operator (add): ")

result = perform_operation(x, y, op)
print(f"Result of {x} {op} {y}: {result}")