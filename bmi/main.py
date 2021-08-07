weight = int(input())
height = float(input())
bmi = round(weight/(height**2), 2)
print(f"{bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
