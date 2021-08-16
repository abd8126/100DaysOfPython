Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	elif(BMI<=18.5):
		print("you are underweight need to eat healthy foods")
	elif(BMI >= 18.5 and BMI < 25):
		print("you are Healthy follow the routine")
	elif(BMI >= 25 and BMI < 30):
		print("you are slighty overweight takes precaution")
    elif BMI >= 30 and BMI < 35 :
	    print("you are severely overweight consult with the doctor")
else:("enter valid details")