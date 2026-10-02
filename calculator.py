def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Basic Calculator ===")
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, try again.")
            continue

        name, func = OPERATIONS[choice]
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        try:
            print(f"{name} result: {func(a, b)}")
        except ValueError as error:
            print(f"Error: {error}")

if __name__ == "__main__":
    main()