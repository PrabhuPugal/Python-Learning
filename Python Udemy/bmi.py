wei=int(input("Weight:"))
he=float(input("Height in metre:"))
bmi=round(wei/(he**2))
if bmi<=18.5:
    print(f'Your BMI is {bmi} and you are underweight')
elif bmi>18.5 and bmi<=24.9:
    print(f'Your BMI is {bmi} and you are healthy')
elif bmi>24.9 and bmi<=29.9:
    print(f'Your BMI is {bmi} and you are overweight')
else:
    print(f'Your BMI is {bmi} and you are obese')
