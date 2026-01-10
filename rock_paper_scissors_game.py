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
---'    ____)____
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

user_choice = input("What you choose? Type 0 for Rock, 1 for paper or 2 for Scissors :")

computer_choice = random.randint(0,2)
print("Computer Choose {computer_choice}")