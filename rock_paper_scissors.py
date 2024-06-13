import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_two = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
player_one = random.randint(0, 2)
print(f"Computer chose : {player_one} ")

if player_one == 0:
    play_1 = rock
elif player_one == 1:
    play_1 = paper
else:
    play_1 = scissors

print(play_1)

if player_two == 0:
    play_2 = rock
elif player_two == 1:
    play_2 = paper
else:
    play_2 = scissors
print("You plays:")
print(play_2)

"""
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""

if play_1 == rock and play_2 == scissors:
    print("Rock wins against scissors.")
    print("You lose!")
elif play_1 == scissors and play_2 == paper:
    print("Scissors win against paper.")
    print("You lose!")
elif play_1 == paper and play_2 == rock:
    print("Paper wins against rock.")
    print("You lose!")
elif play_2 == rock and play_1 == scissors:
    print("Rock wins against scissors.")
    print("You Win!")
elif play_2 == scissors and play_1 == paper:
    print("Scissors win against paper.")
    print("You Win!")
elif play_2 == paper and play_1 == rock:
    print("Paper wins against rock.")
    print("You Win!")
else:
    print("Play again!")
