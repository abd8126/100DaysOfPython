### 1. Write a Python function that takes a list and returns a new list with prime number elements .
def prime(list1):

    list2=list()

    for i in list1:

        q=True

        if i==1 or i==0:

            q=False

        else:

            for j in range(2,i//2+1):

                if i%j==0:

                    q=False

        if q:

            list2.append(i)

    return list2



n=list(map(int,input("enter the values for list:- ").split()))

prime_list=prime(n)

print("List of prime numbers = ",prime_list) 





### 2. Write a Python function to check whether a number is perfect or not.
'''
 def PerfectorNot(n):           
    sum = 0
  
    for i in range(1, n):
        if n% i == 0:
            sum +=  i
    if(sum == n):
        print("Number is perfect")
    else:
        print("Number is not perfect")

number = int(input("Enter the number: "))
PerfectorNot(number)
'''


### 3. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
''' print("entr the input:- ")
words = list(map(str,input().split("-")))
words.sort()
print(words)
'''
### 4. Write a Python function to check whether the given integer is a multiple of both 5 and 7
'''
def MultipleorNot(a):
    number = int(a)
    if(number% 7 ==0 and number % 5 == 0):
        print("Number is multiple of 5 and 7")
    else:
        print("No. is not multiple of 5 and 7")
number = int(input("Enter the number to check:- "))
MultipleorNot(number) 
'''