import string
import random


def genPassword(n):
    # create passwd
    passwd = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) +  \
             random.choice(string.digits) + random.choice(string.punctuation)
    for i in range(n - 4):
        char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        passwd += char
    return passwd


if __name__ == '__main__':
    pd = genPassword(12)
    print(pd)