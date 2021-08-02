import random
import string


length= int(input("Enter the length of the password "))
collection = string.ascii_lowercase +string.ascii_letters+string.ascii_uppercase+string.punctuation
password = ''.join(random.choice(collection) for i in range(length))
print(f"Random password of length {length} is {password}")