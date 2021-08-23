
*1.

list1 = [1, 2, 4, 5, 9]
list1.sort()
print("Largest number in this list is:", list1[-1])



*2.


list1 = [1, 2, 4, 5, 9]
list1.sort()
print("Smallest number in this list is:", *list1[:1])



*3.

def match_words(words):
  a = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      a += 1
  return a

print(match_words(['abc', 'xyz', 'aba', '1221']))



*4.


def anything(n): return n[-1]

def sort_list_anything(tuples):
  return sorted(tuples, key=anything)

print(sort_list_anything([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



*5.


i = [1,2,3,2,1,5,6,4,8,5,4]

dup_items = set()
uniq_items = []
for x in i:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)



*6.


a = []
if not a:
  print("List is empty")



 *7.


original_list = [23, 24, 25, 26, 27]
new_list = list(original_list)
print(original_list)
print(new_list)



*8.


def words(n, str):  
    word_len = []  
    txt = str.split(" ")  
    for x in txt:  
        if len(x) > n:  
            word_len.append(x)  
    return word_len   
print(words(3, "Hello, this is hundred days of python"))
