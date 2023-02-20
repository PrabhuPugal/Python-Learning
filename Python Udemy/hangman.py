import random
# with open("words.txt",'r') as f:
#     lines=f.readlines()
words=['hello','good','nice']
# for word in lines:
#     words.append(word[:-1])
chosen_one=random.choice(words)
length_of_chosen=len(chosen_one)
display=[]
y=0
for _ in range(length_of_chosen):
    display+='_ '
print(''.join(display))
your_input=input("Guess the letter: ")
your_input.lower()
for position in range(length_of_chosen):
    if chosen_one[position]==your_input:
        display[position]=your_input
print(''.join(display))

   
        

    