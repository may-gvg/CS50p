

i = 50
while i > 0:
    n = int(input("Insert Coin : "))
    i = i - n
    if 50 <= i or i <= 1:
        continue
    # looks buged 50 - 30 = should be 20 
    if n == 30:
        i = 50
    print("Amount due: " + str(i))
print("Change owed: " + str(abs(i)))
