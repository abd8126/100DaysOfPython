import random
import array
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',                 #choice for the password and one must be selected form each
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS     #concatination of all to form passworde
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)                                # random selection from each(only one)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp = rand_digit + rand_upper + rand_lower + rand_symbol                    # 4 unit are there in password
for x in range(MAX_LEN - 4):
	temp = temp + random.choice(COMBINED_LIST)                               # adding complete char to password

	temp_list = array.array('u', temp)                                       #shuffle it for more randomness
	random.shuffle(temp_list)

password = ""
for x in temp_list:                                                          # now the final password obtained by adding array and char
		password = password + x

print(password)                                                              # final password
