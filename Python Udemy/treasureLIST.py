import random
r1=["a","b","c"]
r2=["d","e","f"]
r3=["g","h","i"]
r=[r1,r2,r3]
print(f'{r1}\n{r2}\n{r3}')
pos=input("Where to you want to input: ")
listno=pos[0]
element=pos[1]
hor=r[int(listno)]
hor[int(element)]="P"
print(f'Now changed\n{r1}\n{r2}\n{r3}')