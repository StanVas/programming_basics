import random
from string import digits, punctuation, ascii_lowercase, ascii_uppercase

all_combinations = digits + punctuation + ascii_lowercase + ascii_uppercase

password_length = int(input('Enter the password length: '))

password = '' .join(random.sample(all_combinations, password_length))

print(f'This is your password: {password}')
