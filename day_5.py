import string
import random

lower_case_letter_list = list(string.ascii_lowercase)
upper_case_letter_list = list(string.ascii_uppercase)
digits = list(string.digits)
symbols = list(string.punctuation)

print(lower_case_letter_list)
print(upper_case_letter_list)
print(digits)
print(symbols)

passwords_list = []

numbers_of_letters = int(input("How many letters would you like to add to the password? "))
numbers_of_uppers = int(input("How many uppercase letters would you like to add to the password? "))
numbers_of_lowers = numbers_of_letters - numbers_of_uppers
numbers_of_digits = int(input("How many digits would you like to add to the password? "))
numbers_of_symbols = int(input("How many symbols would you like to add to the password? "))

for i in range(numbers_of_lowers):
    passwords_list.insert(random.randint(0, len(passwords_list)), lower_case_letter_list[random.randint(0, len(lower_case_letter_list) - 1)])

for i in range(numbers_of_uppers):
    passwords_list.insert(random.randint(0, len(passwords_list)), upper_case_letter_list[random.randint(0, len(upper_case_letter_list) - 1)])

for i in range(numbers_of_digits):
    passwords_list.insert(random.randint(0, len(passwords_list)), digits[random.randint(0, len(digits) - 1)])

for i in range(numbers_of_symbols):
    passwords_list.insert(random.randint(0, len(passwords_list)), symbols[random.randint(0, len(symbols) - 1)])


passwords = ""
for e in passwords_list:
    passwords += e

print(passwords_list)
print(passwords)

