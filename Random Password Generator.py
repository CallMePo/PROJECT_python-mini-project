import random
import string

length = 12
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("YourPassword: ", password)