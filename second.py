import random
import string
import os

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have selected a number between 1 and 100.")
    
    target_number = random.randint(1, 100)
    attempts = 0
    max_score = 100
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                # Deduct 10 points for every wrong attempt, minimum score is 10
                score = max(10, max_score - ((attempts - 1) * 10))
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                print(f"Your Score: {score}/100")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def word_counter():
    print("\n--- File-Based Word Counter ---")
    filename = input("Enter the name of the text file (e.g., sample.txt): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        print("Please create it in the same folder as this script and try again.")
        return

    word_frequency = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            
            # Basic string manipulation: convert to lowercase and remove punctuation
            text = text.lower()
            for char in string.punctuation:
                text = text.replace(char, '')
                
            words = text.split()
            
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
                    
        print(f"\nTotal words found: {len(words)}")
        print("Top 5 most frequent words:")
        
        # Sort dictionary by frequency in descending order
        sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
        
        for word, count in sorted_words[:5]:
            print(f" - '{word}': {count} times")
            
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    while True:
        print("\n=== PROJECT 02 MAIN MENU ===")
        print("1. Play Number Guessing Game")
        print("2. Run Word Counter & Frequency Analysis")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_counter()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()