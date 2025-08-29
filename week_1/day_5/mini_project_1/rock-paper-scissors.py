from game import Game

def get_user_menu_choice():
    print("\n--- Main Menu ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("x. Quit")
    choice = input("Enter your choice: ").strip().lower()

    if choice in ["1", "2", "x", "q"]:
        return choice
    else:
        print("Invalid choice. Try again.")
        return None

def print_results(results):
    print("\n--- Game Results ---")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            continue

        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == "2":
            print_results(results)

        elif choice in ["x", "q"]:
            print_results(results)
            break

if __name__ == "__main__":
    main()
