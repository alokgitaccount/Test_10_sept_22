print("1............write operation..............")

with open("file.txt", "w") as fp:
    indata = input("enter text: ")
    fp.write(indata)
    fp.close()

print("2.........read operation.................")
with open("file.txt", "r") as fp:
    data = fp.read()
    print(data)
    fp.close()

print("3...........append operation...............")
with open("file.txt", "a") as fp:
    indata = input("enter text: - ")
    fp.write(indata)
   # print(fp.read())   #io.UnsupportedOperation: not readable
    fp.close()

print("4........read and write operation.....")
with open("file.txt", "r+") as fp:
    txtdata = fp.read()
    print(txtdata)
    indata = input("enter text : = ")
    fp.write(indata)
    txtdata2 = fp.read()
    print(txtdata2)

print("5.....w+ read and write ..............")
with open("file.txt", "w+") as fp:
    indata = input("enter data= ")
    fp.write(indata)
    textdata = fp.read()
    print(textdata)

print("6. .....a+...........either we can write from beginning  or append data.. at last..")
with open("file.txt", "a+") as fp6:
    txt = fp6.read()
    print(txt)
    intxt = input("enter data")
    fp6.write(intxt)

print("7......x...write mode exclusively.............")
with open("file.txt", "x") as fp7:
    data = input("enter data : = ")
    txt = fp7.write(data)
    print(txt)
