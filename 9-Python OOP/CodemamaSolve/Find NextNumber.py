s = input()
li = s.split(" ")
li[0] = int(li[0])
li[1] = int(li[1])
li[2] = int(li[2])

if (li[1]-li[0] == li[2]-li[1]):
    print(li[2] + li[1]-li[0])
elif (li[1]/li[0] == li[2]/li[1]):
    print(li[2] * (li[1]/li[0]))