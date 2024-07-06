fileName = "hello.py"

               #a -> append
with open (fileName, "a") as fp:
    fp.write("\ne = 500")

                #w -> write (erase previous + write)
# with open (fileName, "w") as fp:
#     fp.write("\ne = 500")

# For Append / Write mode:
# if the file is not found then new file will create as same name

