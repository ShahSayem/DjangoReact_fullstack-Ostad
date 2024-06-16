# st = set()
st = {1, 2, 3, 4, 5, 6, 6, 6}
print(type(st), st)

st.add(7)


li = [4, 2, 2, 1, 3]
s = set(li)
print(s)

# print(dir(set))


print(2 in s)
print(3 in s)

for item in s:
    print(item)


text = "In the garden, the crimson roses bloomed next to the emerald green shrubs, creating a vibrant display of nature's beauty. The sky was a cerulean blue , contrasting sharply with the golden hues of the setting sun. Nearby, a lavender bush emitted a soothing fragrance, while amber leaves rustled gently in the breeze. A pearl white butterfly fluttered by, landing on a sapphire bluebell, completing the picturesque scene."

colors = ["red", "green", "yellow", "blue", "white", "amber", "black", "golden", "purple"]

clrSet = set()

wordList = text.split(" ")
for word in wordList:
    if (word in colors):
        clrSet.add(word)

print(clrSet)
# print(s[0]) //Error



