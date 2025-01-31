def add(num1, num2):
    """Function to add two numbers."""
    return num1 + num2


def subtract(num1, num2):
    """Function to subtract num2 from num1."""
    return num1 - num2


def multiply(num1, num2):
    """Function to multiply two numbers."""
    return num1 * num2


def divide(num1, num2):
    """Function to divide num1 by num2."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2


def get_numbers():
    """Helper function to get input numbers from the user."""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def calculator():
    """Main calculator function."""
    print("Simple Calculator")

    # Options menu
    options = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
        "5": ("Exit", None)
    }

    while True:
        print("\nChoose an operation:")
        for key, (name, _) in options.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1-5): ")

        if choice in options:
            if choice == '5':  # Exit
                print("Exiting...")
                break

            num1, num2 = get_numbers()

            # Perform the selected operation
            operation_name, operation_func = options[choice]
            try:
                result = operation_func(num1, num2)
                print(f"Result of {operation_name}: {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    calculator()