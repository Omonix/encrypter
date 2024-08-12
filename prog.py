import random
import string

todo = input('\033[1;34mDo you want encrypt or decrypt message ? e/d ')
alphabet = string.printable

def genPassword(length):
    pwd = ""
    i = 0
    while i < int(length):
        pwd = pwd + random.choice(alphabet)
        i = i + 1
    return pwd
def vigenere(message, key, direction=1):
    key_index = 0
    encrypted_message = ''
    for char in message:
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = alphabet.index(key_char)
        index = alphabet.find(char)
        new_index = (index + offset*direction) % len(alphabet)
        encrypted_message += alphabet[new_index]
    return encrypted_message
def decrypt(message, key):
    return vigenere(message, key, -1)
def encrypt(message, key):
    return vigenere(message, key)

if todo == 'e':
    data = input("\033[1;33mMessage to encrypt : \033")
    hasher = genPassword(input('\033[1;36mLength security : '))
    print(f"\033[1;92m\nKey : \033[1;35m{hasher}\n\033[1;92mEncrypted data: \033[1;35m{encrypt(data, hasher)}\033[0m")
elif todo == 'd':
    data = input('\033[1;33mMessage to decrypt : ')
    hasher = input('\033[1;36mKey : ')
    print(f'\033[1;92m\nDecrypted data : \033[1;35m{decrypt(data, hasher)}\033[0m')
else:
    print(f'\033[1;31mError : \'{todo}\'\033[0m')