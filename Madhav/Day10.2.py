def perfect(n):
    s=0
    for i in range(1,n//2+1):
        if n%i==0:
            s+=i
    if s==n:
        return True
    else:
        return False
print("---TO CHECK IF NUM IS PERFECT OR NOT---")
num=int(input("ENTER THE NUM: "))
if perfect(num):
    print("NUMBER IS PERFECT")
else:
    print("NUMBER IS NOT PERFECT")