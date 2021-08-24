#PROGRAM TO REMOVE DUPLICATES
pure_list=[]
lst=list(map(int,input("ENTER THE TERMS SPACE SEPARATED : ").split()))
[pure_list.append(i) for i in lst if i not in pure_list]
print(f"YOUR NEW LIST : {pure_list}")