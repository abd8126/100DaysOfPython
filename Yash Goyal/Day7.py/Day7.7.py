# Python program to clone or copy a list
List = list(map(eval, input("Enter the values:\n ").split()))
lst2 = List.copy()
print("Real list\n ", List)
print("YOUR Copied list\n ", lst2)
