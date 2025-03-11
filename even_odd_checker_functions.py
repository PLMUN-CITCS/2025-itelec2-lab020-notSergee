def get_integer_input() -> int:
    
    while True:
        try:
            number = int(input("Enter an integer: ")) 
            return number
        except ValueError:  
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    
    number = get_integer_input()  
    result = check_even_odd(number)  
    print(result)  

# Run the main program
if __name__ == "__main__":
    main()
