import pyautogui
import random

chars = '1234567890'
char_list = list(chars)
password = pyautogui.password('Enter your test password: ')
guess_password = ''

while guess_password != password:
    guess_password = random.choices(char_list, k=len(password))
    print(f'DECRYPTING {guess_password} PASSWORD')

    if guess_password == list(password):
        print(f"Your password is: {''.join(guess_password)}")
        break
