from random import choice
from string import ascii_letters

orig_msg = input("Enter your message: ")
encod_msg = []
mappings = dict()


for letter in set(orig_msg):

    new_letter = choice(list(ascii_letters) + [' '])
    while new_letter in mappings.keys():
        new_letter = choice(list(ascii_letters) + [' ']) 
    mappings[letter] = new_letter  # encoded letter


for letter in orig_msg:  # encoding the original message letters one by one
    encod_msg.append(mappings[letter])  # adding the mappings letter in the dictionary to the encoded message


print(''.join(encod_msg))  # joins the encoded message into one sting

