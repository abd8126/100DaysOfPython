#BMICalculator
w=int(input("Enter your weight in kgs: "))
h=int(input("Enter your height in metres: "))
bmi = round(float(w)/(float(h)**2))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are normal.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")