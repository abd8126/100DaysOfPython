import random
import array
import string
length_pass = 12
digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

special_char = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
combinations = digits + upper_case + special_char  
Digits = random.choice(digits)
upperChar = random.choice(upper_case)                              
lowerChar = random.choice(lower_char)
specialChar= random.choice(special_char)
temp = Digits + upperChar + lowerChar + specialChar                  
for i in range(length_pass - 4):
	temp = temp + random.choice(combinations)                               
	temp_list = array.array('u',temp)                                      
	random.shuffle(temp_list)

random_password = ""
for i in temp_list:                                                         
		random_password += i
print(random_password)                    