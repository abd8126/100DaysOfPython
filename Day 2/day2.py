print('Welcome to the tip calculator')
bill = float(input('What was the total bill?\n$'))
percentage_tip = int(input('What percentage tip would you like to give? 15, 20 or 25?\n'))
number_of_people = int(input('How many people are  splitting the bill?\n'))
split_pay = (bill + (bill * (percentage_tip / 100))) / number_of_people
print(f"Each person should pay: ${split_pay:.2f} ")
