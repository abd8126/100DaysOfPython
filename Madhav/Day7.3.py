#TO COUNT NO. OF STRING WITH SAME FIRST ND LAST CHAR ND LENGTH GREATER THAN 2
lst=list(map(str,input("ENTER THE TERMS SPACE SEPARATED: ").split()))
count=0
for i in lst :
    if len(i)>2 and i[0]==i[-1]:count+=1
print("THE OUTCOME IS: ",count)