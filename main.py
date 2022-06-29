#Password generator which gives the user the ability to select whether they want to include Upper case letters, Lowercase Letters, numbers and symbols.

import random 

upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters = upper_case_letters.lower() 
numbers = "0987654321"
symbols = "!£$%^&*()-+=/\\@][}{;:?"

upper, lower, numbs, symbls = True, True, True, True 

pw = ""

if upper:
  pw += upper_case_letters
if lower:
  pw += lower_case_letters
if numbs:
  pw += numbers
if symbls:
  pw += symbols

length = 15
amount = 1

for y in range(amount):
  password = "".join(random.sample(pw, length))
print("Password Suggestion ---->  " + password)