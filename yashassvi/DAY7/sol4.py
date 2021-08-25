l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range (0,len(l)):
    for j in range(0, len(l)-i-1):  
                if (l[j][-1] > l[j + 1][-1]):  
                    t = l[j]  
                    l[j]= l[j + 1]  
                    l[j + 1]= t 
print(l)
    
