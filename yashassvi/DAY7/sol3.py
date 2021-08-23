l=['abc','xyz','aba','1221','malayalam','2']
c = 0
for i in l:
    if (len(i) >= 2 and i[0] == i[-1]):
        c=c+1          
print(c)