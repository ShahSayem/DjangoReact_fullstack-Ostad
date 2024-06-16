def findOccurance(s, key):
    sz = len(key)
    sLen = len(s)

    cnt = 0
    for i in range(0, sLen-sz+1):
        if (s[i: i+sz] == key):
            cnt += 1

    return cnt


def cat_dog(str):
    return (findOccurance(str, "cat") == findOccurance(str, "dog"))