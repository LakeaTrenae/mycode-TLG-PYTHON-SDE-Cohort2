import random

def get_answer():
    """Ask the user if the guess is correct and handle simple responses."""
    answer  = input("Is my guess correct? (yes/no/quit): ").strip().lower()
    return answer

def main():
    """Run the color guessing game with simplified logic."""
    # List of colors to guess from
    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white']

    print("Can you guess what color I'm thinking of?:")
    print(", ".join(colors))
    print("Oh this is a piece of cake, of course I can.")

    while True:
        # Randomly pick a color from the list
        guess = random.choice(colors)
        print(f"My guess is: {guess}")

        # Get user answer on the guess
        answer = get_answer()

        if answer == 'yes':
            print(f"Great! I guessed it right. The color you were thinking of is {guess}.")
            break
        elif answer == 'no':
            print("Hmmm, let me guess again....")
        elif answer == 'quit':
            print("Thanks, fr playing with me! Bye!")
            break
        else:
            print("Please respond with a valid  'yes', 'no', or 'quit'.")

if __name__ == "__main__":
    main()
