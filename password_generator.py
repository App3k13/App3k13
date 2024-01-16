import random

characters = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_length = input("Ile znaków ma mieć twoje hasło?")

safe_password = "" 
for i in range(password_lenght):
    safe_password += random.choice(characters)

print(safe_password)
