#Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
n=int(input("ENTER THE TOTAL NO. OF TERMS IN LIST: "))
lst=[]
for i in range(n):
    tpl=tuple(map(int,input("ENTER THE TERMS SPACE SEPARATED: ").split()))
    lst.append(tpl)
for i in range(n):
    for j in range(0,n-i-1):
        if lst[j][-1]>lst[j+1][-1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
print("YOUR SORTED LIST : ")
print(lst)