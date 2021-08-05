h=eval(input("Enter your height(in m)"))
w=eval(input("Enter ypur weight(in kg)"))
x=w/(h*h)
if(x<=18.5):
    print("underweight")
elif(25>=x>18.5):
    print("normal weight")
elif(30>=x>25):
    print("slightly overweight")
elif(35>=x>30):
    print("obese")
else:
    print("clinically obese")