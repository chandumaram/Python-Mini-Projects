import random
import string

length = 10
total = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.sample(total, length))

print(password)