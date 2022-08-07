x = str(input("Item: ")).title()

dicto = {
    "Banana": "110",
    "Apple": "130",
    "Avocado": "50",
    "Kiwifruit": "90",
    "Lemon": "10",
    "Pear": "100",
    "Grapefruit": "60",
    "Sweet Cherries": "100"

}

if dicto.get(x):
    print("Calories: " + str(dicto.get(x)))
else:
    print("")
