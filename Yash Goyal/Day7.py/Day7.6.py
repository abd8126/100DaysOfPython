# Python program to check a list is empty or not
List = list(map(eval, input("Enter the values ").split()))
if len(List) == 0:
    print("List is empty")
else:
    print("List is not empty")
