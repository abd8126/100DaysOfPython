# Python program to get the largest number from a list.
import functools as fun
print("To find maximum number in list:")
l = list(map(int, input("Enter the element space sepearted:\n ").split()))
ele = fun.reduce(lambda a, b: a if a > b else b, l)
print("Maximum no. is :\n", ele)
