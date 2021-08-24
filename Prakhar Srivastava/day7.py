(1)

lis = []

# user enters the number of elements 
count = int(input('How many numbers? '))

# append all input elements in list
for n in range(count):
    number = int(input('Enter number: '))
    lis.append(number)

print("Largest element of the list is :", max(lis))


(2)

lis = []

# user enters the number of elements 
count = int(input('How many numbers? '))

# append all input elements in list
for n in range(count):
    number = int(input('Enter number: '))
    lis.append(number)

print("smallest element of the list is :", min(lis))


(3)


def compare(a):
    ctr = 0
    for i in a:
        if len(i) > 2 and i[0] == i[-1]:
            ctr+= 1
    return ctr

a = ['abc', 'xyz', 'aba', '1221']
for i in a:
    z = compare(a)

print(z)


(4)



def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

 #sir i copy this ans from google i thought this is more relevent way to solve this question ..



(5)


a = [2, 3, 3, 2, 5, 4, 4, 6]
 
b = []
 
for i in a:
    
    if i not in b:
        b.append(i)
 
print(b)

# manoj sir thought us this way to do this 



(6)


find_the_list = []


if len(find_the_list):
	print('The list is not empty')
else:
	print('T list is empty')




(7)


list1 = [11,22,33,44,55,66,77,88]
print('Old list: ',list1)
# Now we  clone list1 to list2
list2 = list1[:]
# Now we print cpied list2
print('New coppied list: ',list2)


(8)



n = int(input)("enter the length of string")
 list1 = [i for i in input().split(",")]
 word_list = []   
 for x in list1:  
     if len(x) > n:  
         word_list.append(x)  

 print(word_list)