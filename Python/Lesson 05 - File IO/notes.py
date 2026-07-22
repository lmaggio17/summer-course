import random


def play_game():
    choices = ["Rock", "Paper", "Scissors"]

    computer_pick = random.choice(choices)
    user_pick = input("Pick Rock, Paper, or Scissors: ").title()

    print(f"You picked: {user_pick}")
    print(f"The computer picked: {computer_pick}")

    if user_pick not in choices:
        print("That is not a valid choice.")
        return "invalid"

    elif user_pick == computer_pick:
        print("It's a tie!")
        return "tie"

    elif (
        (user_pick == "Rock" and computer_pick == "Scissors")
        or (user_pick == "Paper" and computer_pick == "Rock")
        or (user_pick == "Scissors" and computer_pick == "Paper")
    ):
        print("You win this round!")
        return "player"

    else:
        print("The computer wins this round!")
        return "computer"


games = int(input("Choose best of 1, 3, 5, 7, or 9: "))

while games not in [1, 3, 5, 7, 9]:
    games = int(input("Invalid choice. Enter 1, 3, 5, 7, or 9: "))

wins_needed = (games // 2) + 1

player_wins = 0
computer_wins = 0
round_number = 1

while player_wins < wins_needed and computer_wins < wins_needed:
    print(f"\nRound {round_number}")

    result = play_game()

    if result == "player":
        player_wins += 1
        round_number += 1

    elif result == "computer":
        computer_wins += 1
        round_number += 1

    elif result == "tie":
        print("Ties do not count. Replay the round.")

    print(f"Score: You {player_wins} - {computer_wins} Computer")


if player_wins == wins_needed:
    print("\nYou won the game!")
else:
    print("\nThe computer won the game!")