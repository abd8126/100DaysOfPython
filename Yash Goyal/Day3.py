# PROGRAM TO CHECK BODY MASS INDEX
print("To check body mass index:")
h = float(input("Enter height in meter:\n"))
w = float(input("Enter weight in kgs:\n"))
bmi = w/h**2
if bmi < 18.5:
    print("Under weight")
elif bmi > 18.5 and bmi < 25:
    print("Normal weight")
elif bmi > 25 and bmi < 30:
    print("Over weight")
elif bmi > 30 and bmi < 35:
    print("Obese.")
elif bmi > 35:
    print("Clinically obese.")
