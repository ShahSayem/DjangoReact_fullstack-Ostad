fileName = "E:\\Programming\\Development\\WebDev\\DjangoReact_fullStack_Ostad\\8-Python OOP\\Live Class\\Pictures\\ssa.jpeg"
file2 = "copy_ssa.jpeg"

        #rb -> read binary file
with open(fileName, "rb") as fp:
    content = fp.read()
    # print(type(content))
    # print(content)

       #wb -> write binary file
    with open(file2, "wb") as fp2:
        fp2.write(content)

print("Task complete!")