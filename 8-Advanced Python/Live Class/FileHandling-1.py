fileName = "hello.py"

try:               #rt -> read
    fp = open(fileName, "rt")

    content = fp.read()
    # content = fp.readline()
    # content = fp.readlines()
    print(content)

    fp.close()
except FileNotFoundError:
    print("Check if the file name is correct and if the file exists")
except Exception as e:
    print(f"An error occurred: {e}")