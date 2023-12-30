import random
length = int(input('Enter the password length: '))

password = ''
i = 1
while i <= length:
    number = random.randint(22,123)
    char = chr(number)
    password += char
    i += 1

print(password)
