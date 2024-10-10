import random
import math

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special = "!@#$%^&*()+"

# pass_len = random.randint(8,13) #without user input
pass_len = int(input("Enter Password Length(>=8): "))

if pass_len<8:
    print("Password length must be 8 or more")
else:
    # length of the password devided by 50-30-20 formulea 
    alpha_len = int(pass_len/2)
    num_len = math.ceil(pass_len*30/100)
    special_len = pass_len - (alpha_len+num_len)

    password_list = []

    def generate_pass(array, length):
        for i in range(length):
            char = random.choice(array)
            password_list.append(char)
    
    # alpha password
    generate_pass(alpha, alpha_len)
    # num pass
    generate_pass(num, num_len)
    # special pass
    generate_pass(special, special_len)

    # shuffle the generated password
    random.shuffle(password_list)

    password = ''.join(password_list)
    print(password)
