lis = []
count = int(input('How many numbers? '))
for n in range(count):
    number = int(input('Enter number: '))
    lis.append(number)
print("Largest element of the list is :", min(lis))