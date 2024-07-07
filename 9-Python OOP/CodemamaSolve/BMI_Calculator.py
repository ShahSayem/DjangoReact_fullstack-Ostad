s = input()

li = s.split(" ")
height = float(li[0])
weight = float(li[1])

bmi = round(weight / (height**2), 2)

print(f"BMI: {bmi}")

if (bmi < 18.5):
    print( "Underweight")
elif (bmi >= 18.5 and bmi < 25):
    print("Normal weight")
elif (bmi >= 25 and bmi < 30):
    print("Overweight")
else:
    print("Obese")