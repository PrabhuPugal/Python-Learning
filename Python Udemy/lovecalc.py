boy=input("Enter the name of the boy: ")
girl=input("Enter the name of the girl: ")
boy=boy.lower()
girl=girl.lower()
nT=boy.count("t")+girl.count("t")
nR=boy.count("r")+girl.count("r")
nU=boy.count("u")+girl.count("u")
nE=boy.count("e")+girl.count("e")
nL=boy.count("l")+girl.count("l")
nO=boy.count("o")+girl.count("o")
nV=boy.count("v")+girl.count("v")
nE1=boy.count("e")+girl.count("e")
Tru=nT+nR+nU+nE
Lov=nL+nO+nV+nE1
lp=str(Tru)+str(Lov)
if int(lp)<10 or int(lp)>90:
    print("Nope!")
elif int(lp)>=40 and int(lp)<=50:
    print("Perfect!")
else:
    print(f"Your love score is {lp}")
