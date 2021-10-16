import random

user_input = int(input("choose 1 for rock, 2 for paper and 3 for scissors\n"))
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
comp_input = random.randint(0, 2)
mapping = [rock, paper, scissors]
if user_input == 1:
    print(f"you choose{mapping[0]}")
    print(f"computer choose{mapping[comp_input]}")
    if comp_input == 0:
        print(f"you and computer had a tie")
    elif comp_input == 1:
        print(f"computer wins!")
    else:
        print(f"you win!")

elif user_input == 2:
    print(f"you choose{mapping[1]}")
    print(f"computer choose{mapping[comp_input]}")
    if comp_input == 0:
        print(f"you win!")
    elif comp_input == 1:
        print(f"you and computer had a tie")
    else:
        print(f"computer wins!")
else:
    print(f"you choose{mapping[2]}")
    print(f"computer choose{mapping[comp_input]}")
    if comp_input == 0:
        print(f"computer wins")
    elif comp_input == 1:
        print(f"you win!")
    else:
        print(f"you and computer had a tie")
