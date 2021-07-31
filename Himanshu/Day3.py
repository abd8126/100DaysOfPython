BMI = eval(input())
if BMI <18.5:
    print("UNDERWEIGHT")
elif BMI <25:
    print("A NORMAL WEIGHT")
elif BMI < 30:
    print("SLIGHTLY OVERWEIGHT")
elif BMI < 35:
    print("OBESE")
else:
    print("CLINICALLY OBESE")