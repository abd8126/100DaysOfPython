
# Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
n = int(input("Enter the total number of terms in list: "))
list = []
for i in range(n):
    tpl = tuple(map(int, input("Enter the terms space separated:\n").split()))
    list.append(tpl)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j][-1] > list[j+1][-1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
print("Your sorted list:\n ")
print(list)
