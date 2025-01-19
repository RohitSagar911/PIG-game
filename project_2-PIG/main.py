from random import randint

def roll():
    dice = randint(1,6)
    return dice


def game(players):
    print("\nLet's start!\n")
    max_score = 50
    player_scores = [0] * players
    print("Initial scores:", player_scores)

    while True:
        for player_idx in range(players):
            print(f"\nPlayer {player_idx + 1}'s turn!")
            print(f"Current total score: {player_scores[player_idx]}")
            current_score = 0

            while True:
                roll_input = (
                    input("Would you like to roll the dice? (y/n): ").strip().lower()
                )
                if roll_input != "y":
                    break

                dice_value = roll()
                if dice_value == 1:
                    print("You rolled a 1! Turn ends with no score.")
                    current_score = 0
                    break
                else:
                    current_score += dice_value
                    print(f"You rolled: {dice_value}")
                    print(f"Current turn score: {current_score}")

            player_scores[player_idx] += current_score
            print(
                f"Total score for Player {player_idx + 1}: {player_scores[player_idx]}"
            )

            if player_scores[player_idx] >= max_score:
                print("\nGame Over!")
                print("Final scores:", player_scores)
                print(
                    f"Player {player_idx + 1} wins with a score of {player_scores[player_idx]}!"
                )
                return  # End the game immediately


while True:
    print("Welcome to PIG!")

    ask_User = input("Do you Want to play the Game?(yes/no)").lower()
    if ask_User != "yes":
        print("Goodbye!")
        quit()

    while True:
        try:
            players = int(input("How many players are playing the game: "))
            if players > 6 or players < 2:
                print("There must be a minimum of 2 and a maximum of 6 players to play this game!")
                print("Please choose again")
            else:
                break  # Exit the loop if the input is valid
        except ValueError:
            print("Please enter a valid number!")

    game(players)
