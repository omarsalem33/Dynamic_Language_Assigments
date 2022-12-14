import string
import random

N = 5
res = ''.join(random.choices(string.ascii_letters, k=N))
print("The generated random string : " + str(res))