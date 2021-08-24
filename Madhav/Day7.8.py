#Python program to find the list of words that are longer than n from a given list of words
lst=list(map(str,input("ENTER THE TERMS SPACE SEPARATED : ").split()))
n=int(input("ENTER THE VALUE OF n: "))
l=[i for i in lst if len(i)>n]
print(f"TOTAL NO. OF WORDS LONGER THAN {n} ARE {len(l)}")