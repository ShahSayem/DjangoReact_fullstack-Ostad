###### List:

#1.Write a function that takes only a list of integers and return a new list that contains only even number of the original list. 

def getEven(numbers):
    # even = []
    # for num in numbers:
    #     if (num%2 == 0):
    #         even.append(num)

    even = [num for num in numbers if num%2 == 0]

    return even


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = getEven(li)

print(ans)



#2. reverse all elements of an list of strings.

def revStrList(strList):
    #[start:stop:step]
    li = [curr[::-1] for curr in strList]

    # for curr in strList:
    #     curr = curr[::-1]
    #     li.append(curr)

    return li


myList = ["Bangladesh", "Nepal", "Bhutan", "Srilanka"]
print(revStrList(myList))



###### Touples:

#3. write a function that takes a list of touples, each touple contains two integers 
# and returns a list of touples with swap elements.

def swapListTouple(liTouple):
    ans = [(curr[1], curr[0]) for curr in liTouple]

    return ans


myListTouple = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]
print(swapListTouple(myListTouple))



###### Dictionary:

#4. Take 2 dictionaries and merge them into one (if same key belongs to both dictionary take the second one)

def mergeDictionary(dt1, dt2):
    # ans = {}
    # for k1, v1 in dt1.items():
    #     ans[k1] = v1

    # for k2, v2 in dt2.items():
    #     ans[k2] = v2

    ans = dt1
    ans.update(dt2)

    return ans


dt1 = {2: "two", 3: "three", 4: "four1"}
dt2 = {1: "one", 2: "two", 4: "four2", 5: "five", 6: "six"}

print(mergeDictionary(dt1, dt2))


###### Set:

#5. Take 2 sets and return common values.

def commonSet(st1, st2):
    # ans = set()
    # for curr1 in st1:
    #     for curr2 in st2:
    #         if (curr1 == curr2):
    #             ans.add(curr1)

    # return ans

    return st1.intersection(st2)

st1 = {2, 3, 5, 7, 11}
st2 = {1, 3, 5, 7, 9}

print(commonSet(st1, st2))
