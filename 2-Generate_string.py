import random
import string

Result = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k = 5))
print("Your Generated String is: " + Result)