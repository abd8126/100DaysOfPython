# Python program to find the list of words that are longer than n from a given list of words
List = list(map(str, input("Enter the terms:\n ").split()))
n = int(input("Enter the valus of n: "))
l = [i for i in List if len(i) > n]
print(f"Total number of words longer than {n} are {len(l)}")
