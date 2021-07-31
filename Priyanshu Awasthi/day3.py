weight = input("Enter the weight in kilogram :")
height = input("Enter the height in centimeters :")
BMI= weight/ (height/100)**2
if BMI < 18.5 :
    print("You are underweight")
elif BMI >= 18.5 and BMI < 25 :
    print("You are Having Normal BMI")
elif BMI >= 25 and BMI < 30 :
    print("You are slightly overwirght ")
elif BMI >= 30 and BMI < 35 :
    print("You are Obese")
elif BMI >= 35 :
    print("You are clinically obese ")