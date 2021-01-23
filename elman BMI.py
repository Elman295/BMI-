print("welcome to elman BMI")
weight=float(input("Enter your weigt(kg):"))
height=float(input("Enter your height(m):"))

BMI=weight//height**2
print(BMI)

if BMI<18.5:
    print("you are thin")
    print("worrning")
elif 18.5<BMI<24.9:
    print("you are healthy")
elif 24.9<BMI<29.9:
    print("worrning")
    print("some extra weight")
elif 29.9<BMI<34.9:
    print("you are fat")
elif 34.9<BMI<40:
    print("very fat becareful")
else:
    print("you are illness")
