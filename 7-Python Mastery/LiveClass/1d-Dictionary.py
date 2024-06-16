text = "In the garden, the crimson roses bloomed next to the emerald green shrubs, creating a vibrant display of nature's beauty. The sky was a cerulean blue , contrasting sharply with the golden hues of the setting sun. Nearby, a lavender bush emitted a soothing fragrance, while amber leaves rustled gently in the breeze. A pearl white butterfly fluttered by, landing on a sapphire bluebell, completing the picturesque scene. green horse with a dunky"

colors = ["red", "green", "yellow", "blue", "white", "amber", "black", "golden", "purple"]

clrDt = {}

wordList = text.split(" ")
for word in wordList:
    if (word in colors):
        if (word in clrDt):
            clrDt[word] += 1
        else:
            clrDt[word] = 1

print(type(clrDt), clrDt)


    #key  val
dt = {1: "one", 2: "two", 3: "three"}
print(dt[1])
print(dt.keys(), dt.values())

for k, v in dt.items():
    print(k, v)

for t in dt.items():
    print(type(t), t)


dt2 = {"one": 1, "two": 2, "three": 3}
for k, v in dt2.items():
    print(k, v)

print(dt2["three"])