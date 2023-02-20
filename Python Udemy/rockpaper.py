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
computer=[rock,paper,scissors]
p1=input("Enter your choice\n0 for rock\n1 for paper\n2 for scissor\n")
cc=random.choice(computer)
if int(p1)==0 and cc==rock:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n Match Draw!")
elif int(p1)==0 and cc==scissors:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You won!")
elif int(p1)==0 and cc==paper:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You Lose!")
elif int(p1)==1 and cc==rock:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You Win!")
elif int(p1)==1 and cc==paper:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n Match Draw!")
elif int(p1)==1 and cc==scissors:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You lose!")
elif int(p1)==2 and cc==rock:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You Lose!")
elif int(p1)==2 and cc==paper:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n You win!")
elif int(p1)==2 and cc==scissors:
    print(f"Your chose:\n{computer[int(p1)]}\nComputer chose:\n{cc}\n Match Draw!")