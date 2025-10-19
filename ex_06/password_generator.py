import random
import string
length = int(input("Enter the desired password length: "))
if length < 4:
    print("Password length should be at least 4 characters.")
    exit()
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(all_characters, k=length))
print(f"Generated password: {password}")