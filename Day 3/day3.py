height = input("Enter height in mtr.: ")
weight = input("Enter weight in kgs : ")

try:
    bmi = round(float(weight)/(float(height)**2))

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
except ValueError:
    print("Enter integer or float values only.")
