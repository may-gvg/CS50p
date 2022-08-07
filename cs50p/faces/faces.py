message = input()
words = message.split()
faces = {":)": "🙂", ":(": "🙁"}

emoji = ""
for word in words:
    emoji += faces.get(word, word) + " "
print(emoji)
