#1
# list = []
# list_len= int(input("Enter the length of list"))
# print("Enter the numbers:")
# for i in range(0,list_len):
#     numbers= int(input())
#     list.append(numbers)
# print("list of numbers",list)
# print("Largest numbers in list: ",max(list))

#2

''' list = []
list_len= int(input("Enter the length of list"))
print("Enter the numbers:")
for i in range(0,list_len):
    numbers= int(input())
    list.append(numbers)
print("list of numbers",list)   
print("smallest numbers in list: ",min(list)) '''

#3


#  list1 = [i for i in input().split(",")]
# result = 0
# for x in list1:
#     if len(x)>1 and x[0] == x[-1]:
#         result += 1
# print(result)  

#4



# touple = int(input("Enter no of tuple group : "))
# list=[]
# for r in range (touple):
#     tup = tuple(map(int,input().split(" ")))
#     list.append(tup)
# print(list)
# lst=len(list)
# for i in range (0,lst):
#     for j in range(0, lst-i-1):  
#                 if (list[j][-1] > list[j + 1][-1]):  
#                     temp = list[j]  
#                     list[j]= list[j + 1]  
#                     list[j + 1]= temp 
# print(list) 




#5


# a = list(input("Enter the elements: "))
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)


#6

# empty = []
# list = list(input("Enter the list"))
# if list == empty:
#     print("list is empty please enter the elements")
# else:
#     print(list)


#7

# original_list= [i for i in input("enter the list" ).split(",")]
# clone = list(original_list)
# print(original_list)
# print(clone)

#8
# n = int(input)("enter the length of string")
# list1 = [i for i in input().split(",")]
# word_list = []   
# for x in list1:  
#     if len(x) > n:  
#         word_list.append(x)  

# print(word_list)

