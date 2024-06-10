li = [1, 2, 3]
li2 = [5, 6, 7]

#li += li2 OR

li.extend(li2)
print(li)

        #idx val
li2.insert(1, 0)
print(li2)

if (5 in li2):
    print(li2.index(5))

if (3 in li):
    li.remove(3)
print(li)

li.pop()
print(li)

    #idx
li.pop(0)

li.sort(reverse=True)
print(li)
