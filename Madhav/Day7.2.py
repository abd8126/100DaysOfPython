#Python program to get the smallest number from a list
import functools as fun
print("TO FIND THE SMALLEST NUM IN LIST:::")
lst=list(map(int,input("ENTER THE ELEMENTS SPACE SEPARATED: ").split()))
ele=fun.reduce(lambda a,b:a if b>a else b,lst)
print("SMALLEST NUM IS:",ele)