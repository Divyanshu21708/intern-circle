import csv
import os

FILE_NAME = 'expenses.csv'
HEADERS = ['Date', 'Category', 'Amount', 'Description']

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_expense():
    print("\n--- Add New Expense ---")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport, Utilities): ").title()
    description = input("Enter a brief description: ")
    
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
            
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added successfully!")

def view_expenses(filter_category=None):
    print(f"\n--- View Expenses {'(Filtered: ' + filter_category + ')' if filter_category else ''} ---")
    
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            
            if not expenses:
                print("No expenses recorded yet.")
                return
            
            found = False
            for row in expenses:
                if filter_category and row['Category'] != filter_category:
                    continue
                found = True
                print(f"Date: {row['Date']} | Category: {row['Category']} | Amount: ${row['Amount']} | Desc: {row['Description']}")
                
            if not found and filter_category:
                print(f"No expenses found for category: {filter_category}")
                
    except FileNotFoundError:
        print("Error: No expense file found.")

def summary_statistics():
    print("\n--- Category Summary Statistics ---")
    category_totals = {}
    total_spent = 0.0
    
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row['Amount'])
                category = row['Category']
                
                total_spent += amount
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
                    
            if total_spent == 0:
                print("No expenses recorded to summarize.")
                return
                
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
            print("-" * 30)
            print(f"Total Expenses: ${total_spent:.2f}")
            
    except FileNotFoundError:
        print("Error: No expense file found.")

def main():
    initialize_file()
    
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. View Summary Statistics")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter category to filter by: ").title()
            view_expenses(filter_category=category)
        elif choice == '4':
            summary_statistics()
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 5.")

if __name__ == "__main__":
    main()