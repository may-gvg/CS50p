import validators

value = input("What's your email address? ")

if not validators.email(value):
    print ("Invalid")
else: print("Valid")