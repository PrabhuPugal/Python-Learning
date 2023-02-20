height=input("Enter the height of the student: ").split(" ")
total_height=0
no_of_students=0
maximum_height=0
for x in height:
    total_height+=int(x)
    no_of_students+=1
    if int(x)>int(maximum_height):
        maximum_height=x
print(maximum_height)
print (total_height/no_of_students)

