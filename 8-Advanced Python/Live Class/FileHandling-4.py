#if different directory, give the full directory
fileName = "hello.py"

with open (fileName, "r+") as fp:
    content = fp.read()
    print(content)

    fp.write("\nx = 900")
    content = fp.read()
    print(content) #write successfully but not getting the update


with open (fileName, "r+") as fp:
    content = fp.read()
    print(content) #Open again to get update

    # print(dir(fp))