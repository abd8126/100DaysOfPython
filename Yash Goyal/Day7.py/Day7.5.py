
# PROGRAM TO REMOVE DUPLICATES
pure_list = []
list = list(map(int, input("Enter the terms:\n ").split()))
[pure_list.append(i) for i in list if i not in pure_list]
print(f"YOUR NEW LIST : {pure_list}")
