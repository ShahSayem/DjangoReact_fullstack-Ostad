fw = open("myFile.txt", "w") #Clear previous txt

fw.write("This is the beginning\n")

lines = ["Apple\n", "Banana\n", "Coconut\n"]
fw.writelines(lines)

fw.close()



fa = open("myFile.txt", "a") #Append after previous txt

fa.write("This is the append\n")

fa.close()



fr = open("myFile.txt", "r")

content = fr.read()
print(content)

fr.close()