
Weight = float(input("Weight in KG: "))
height = float(input("height in meter: "))
BMI_Index=Weight/height**2
if(BMI_Index < 18.5):
    print("you are underweight")
elif(BMI_Index<25):
     print("Your have normal weight")
elif(BMI_Index < 30):
    print("you are below overweight")
elif(BMI_Index < 35):
    print("you are overweight, Please do excersice and other stuff")
elif(BMI_Index > 35):
    print("You are clinically obese")