# Question 1: Write a Python program to get the largest number from a list.


 
L =list(map(int,input().split()))

L.sort()

print(L[len(L)-1])




# QUESTION 2: Write a Python program to get the smallest number from a list.



L =list(map(int,input().split()))

L.sort()

print(L[0])




''' QUESTION 3: Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2 '''



L =list(map(str,input().split()))

c=0

for i in L:

    if(len(i)==2):

        if(i[0]==i[1]):

            c+=1

    elif(len(i)>2):

        if(i[0]==i[len(i)-1]):

            c+=1

print(c)





''' Question 4: Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] '''





L=list(map(tuple,input().split()))
for j in range (1,len(L)) :
    for i in range(len(L)-j) :
        if a[i][1]>a[i+1][1] :
            temp=L[i]
            L[i]=L[i+1]
            L[i+1]=temp
for i in range(len(L)) :
    print(L[i])



# Question 5: Write a Python program to remove duplicates from a list.




L =list(map(str,input().split()))

L1 = set(L)

print(list(L1))





#Question 6: Write a Python program to check a list is empty or not



L =list(map(str,input().split()))
l1=[]
if L==l1:

    print("List is empty")

else:

    print("List is not empty")





# Question 7: Write a Python program to clone or copy a list.



L =list(map(str,input().split()))

L2=L.copy()

print("The copied list is :- ",L2)




#Question 8: Write a Python program to find the list of words that are longer than n from a given list of words.



L =list(map(str,input().split()))

W = input()

c=0

for i in L:

    if(len(i)>len(W)):

        c+=1 

print(c) 

