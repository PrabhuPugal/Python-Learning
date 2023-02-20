import random
HorT=random.randint(0,1)
if HorT==0:
    print("heads")
else:
    print("tails")

names=input("Enter names separated with commas and space: ")
string=names.split(", ")
print(string)
picker=random.choice(string)
print(picker)