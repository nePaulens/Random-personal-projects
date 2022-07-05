#!/usr/bin/env python

import sys, random, string

service = str(input('\nEnter website: '))
username = str(input('\nEnter username: '))
length = int(input('\nEnter length: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
sym = string.punctuation

all = lower + upper + num + sym

temp = random.sample(all, length)

password = "".join(temp)

file = open("passwords.txt", "a")
file.write("Service: " + service + "\nUsername: " + username + "\nPassword: " + password + "\n----------------------------------------------\n")
file.close()

print("\nSuccess!")