weight= float(input("Enter the weight in kiligrams : "))
height= float(input("Enter the height in centimetres : "))
BMI = weight / (height/100)**2
if BMI < 18.5 :
    print("You are underweight")
elif BMI >= 18.5 and BMI < 25 :
    print("You are Normal BMI")
elif BMI >= 25 and BMI < 30 :
    print("You are slightly overweight")
elif BMI >= 30 and BMI < 35 :
    print("Yor are Obese") 
elif BMI >= 35 :
    print("You are clinically obese")
print(BMI)
# BODY MASS INDEX CALCULATOR 
# DO EXERCISE DAILY 