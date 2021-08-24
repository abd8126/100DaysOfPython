# Python program to get the smallest number from a list.
import functools as fun
print("To find smallest number in list:")
lst = list(map(int, input("Enter the element space sepearted:\n ").split()))
ele = fun.reduce(lambda a, b: a if b > a else b, lst)
print("Smallest no. is:\n", ele)
