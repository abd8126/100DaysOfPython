#PROGRAM TO CHECK BODY MASS INDEX
print("TO CHECK BODY MASS INDEX:")
w=eval(input("ENTER YOUR WEIGHT IN kgs: "))
h=eval(input("ENTER YOU HEIGHT IN meter: "))
bmi=w/(h*h)
if bmi<18.5:
    a="Under Weight"
elif bmi>18.5 and bmi<25:
    a="Normal weight"
elif bmi>24.9 and bmi<30:
    a="Over weight"
elif bmi>29.9 and bmi<35:
    a="Obesity Class I"
elif bmi>34.9 and bmi<40:
    a="Obesity class II"
else:
    a="Obesity class III"
print("Weight Status : "+a)