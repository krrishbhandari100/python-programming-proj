import string
import random
letters = list(string.ascii_letters)
num = list(string.digits)
punc = list(string.punctuation)
all_l = []
all_l.extend(letters)
all_l.extend(num)
all_l.extend(punc)
len_of_pass = int(input("Enter the password length: "))
for i in range(0, len_of_pass):
    print(random.choice(all_l), end='')