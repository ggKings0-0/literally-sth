import random
number_of_passwords = int(input("Enter amount of passwords you need: "))
number_of_letters = int(input("Enter number of symbols in password: "))
for i in range(number_of_passwords):
    password = ""
    for j in range(number_of_letters):
        password += random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@$#%^&*'))
    print(password)
