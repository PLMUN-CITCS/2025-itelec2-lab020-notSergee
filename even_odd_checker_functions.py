def get_integer_input() -> int:
    """
    Prompts the user to input an integer and returns the integer value.
    Ensures that the input is a valid integer.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter an integer: "))  # Try converting input to integer
            return number
        except ValueError:  # If input is not a valid integer, handle the exception
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Checks if the number is even or odd using the modulo operator.
    
    Args:
        number (int): The number to be checked.
    
    Returns:
        str: A string stating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main function to run the program. Gets user input and displays whether the number is even or odd.
    """
    number = get_integer_input()  # Get the integer input from the user
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Display the result

# Run the main program
if __name__ == "__main__":
    main()
