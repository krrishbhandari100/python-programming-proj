import random
string = input("Enter the string you want to manuplate: ")
string = list(string)
for i in range(0, len(string)):
    print("" .join(random.sample(string, len(string))))

input()
# this above input is to hold the screen when running from directory
