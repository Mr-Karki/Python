# Best of 3 for rock, paper, scissors game

import random # This statement makes the functions defined in the random module available for use

print("Let's play rock, paper, or scissors")

player_wins = 0
computer_wins = 0

#for player to choose
while player_wins < 2 and computer_wins < 2:
  player_choice = input("\nChoose rock, paper, or scissors: ").lower()
  choices = ["rock", "paper", "scissors"]

#for computer to choose
  computer_choice = random.choice(choices)
  print(f"Computer chose: {computer_choice}")

#condition to win match
  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
  elif player_choice == computer_choice:
    winner = "Tie"
  else:
    winner = "Computer"

#condition to track first to win two match
  if winner == "Player":
    player_wins += 1
    print("You won")
  elif winner == "Computer":
    computer_wins += 1
    print("Computer won")
  else:
    print("It's a tie")
  print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
    print("Computer won!")