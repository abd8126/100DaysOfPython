
Weight = float(input("Weight in KG: "))
height = float(input("height in meter: "))
BMI=Weight/height**2
if(BMI < 18.5):
    print("you are underweight")
elif(BMI<25):
     print("Your have normal weight")
elif(BMI < 30):
    print("you are below overweight")
elif(BMI < 35):
    print("you are overweight, Please do excersice and other stuff")
elif(BMI > 35):
    print("You are clinically obese")
print(BMI)