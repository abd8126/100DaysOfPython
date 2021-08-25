
# TO COUNT NO. OF STRING WITH SAME FIRST ND LAST CHAR ND LENGTH GREATER THAN 2
list = list(map(str, input("Enter the term ").split()))
count = 0
for i in list:
    if len(i) > 2 and i[0] == i[-1]:
        count += 1
print("THE OUTCOME IS: ", count)
