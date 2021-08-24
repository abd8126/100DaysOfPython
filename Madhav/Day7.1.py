#Python program to get the largest number from a list.
import functools as fun
print("WELCOME...TO FIND THE MAX NO. IN LIST:::")
l=list(map(int,input("ENTER THE ELEMENT OF LIST SPACE SEPARATED: ").split()))
ele=fun.reduce(lambda a,b:a if a>b else b,l)
print("MAXIMUM NUM IS :",ele)