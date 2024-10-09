#Simple random password generator using lists, random module, and loops
import random
#list of letters,numbers, symbols that will be used to generate the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#variable for number of letter,symbols & numbers to be generated in the password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#blank list created to hold the values that will be generated randomly in below for loop
password_list = []
#random values (n = user input) will be appended to above list, values will be taken from list at top (letters, numbers, symbols)
for char in range (0,nr_letters):
    password_list.append(random.choice(letters))
for sym in range (0,nr_symbols):
    password_list.append(random.choice(symbols))
for numb in range (0,nr_numbers):
    password_list.append(random.choice(numbers))
#shuffling the generated random results
random.shuffle(password_list)
#then using .join to convert it to string
password = "".join(password_list)
print(f"Generated Password is: {password}")