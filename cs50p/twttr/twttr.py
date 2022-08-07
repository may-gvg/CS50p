import re

x = input("Input: ")
mass = re.sub(r'[aeiouAEIOU]', '', x)
print("Output: " + str(mass))