fileName = "hello.py"

try:
    fp = open(fileName, "rt")

    # content = fp.read()
    # content = fp.readline()
    content = fp.readlines()
    print(content)

    fp.close()
except FileNotFoundError:
    print("Check if the file name is coorect and if the file exists")