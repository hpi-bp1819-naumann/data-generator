import random

def random_string(a):
    str = ''
    for i in range(10):
        str += chr(random.randrange(65,90))
    return "'" + str + "'"
