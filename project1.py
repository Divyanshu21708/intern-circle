def arithmetic_calculator():
    while True:
        print("\n--- Basic Arithmetic ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Go Back")
        
        choice = input("Select an operation (1-5): ")
        
        if choice == '5':
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice. Please select a valid option.")

def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. USD to EUR (Currency)")
        print("4. Go Back")
        
        choice = input("Select a conversion (1-4): ")
        
        if choice == '4':
            break
            
        if choice in ['1', '2', '3']:
            try:
                value = float(input("Enter the value to convert: "))
                
                if choice == '1':
                    miles = value * 0.621371
                    print(f"{value} km is equal to {miles:.2f} miles.")
                elif choice == '2':
                    fahrenheit = (value * 9/5) + 32
                    print(f"{value}°C is equal to {fahrenheit:.2f}°F.")
                elif choice == '3':
                    # Assuming a fixed exchange rate for simplicity
                    eur = value * 0.85 
                    print(f"${value} USD is equal to €{eur:.2f} EUR.")
            except ValueError:
                print("Invalid input! Please enter a numerical value.")
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Arithmetic Calculator")
        print("2. Unit & Currency Converter")
        print("3. Exit")
        
        choice = input("What would you like to do? (1-3): ")
        
        if choice == '1':
            arithmetic_calculator()
        elif choice == '2':
            unit_converter()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()