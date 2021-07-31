print("Welcome to the BMI Calculator")
w=float((input("Please enter your weight in kilograms: ")))
h=float((input("Please enter your height in metres: ")))
bmi=w/(h*h)
if (bmi < 18.5):
    print("You come under the category of 'Underweight'.\nYou're adviced to increase your caorie intake.")
elif (bmi >= 18.5) and (bmi < 25):
    print("You come under the category of 'Normal BMI'.\nYou're adviced to maintain your current lifestyle.")
elif (bmi >= 25) and (bmi < 30):
    print("You come under the category of 'Slightly Overweight'.\nA little excercise would help.")
elif (bmi >= 30) and (bmi < 35):
    print("You come under the category of 'Obese'.\nYou're adviced to make some serious positive changes in your lifestye.")
elif (bmi >= 35):
    print("You come under the category of 'Clinically Obese'.\nYou're adviced to see a doctor and get a checkup.")