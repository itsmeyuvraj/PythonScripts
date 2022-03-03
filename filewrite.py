files = open("file.txt",mode="w")



con = input("Write something: ")
files.write(con)
files.flush()
files.close()


filess=open("file.txt",mode="r")


for n in filess:
    print(n)




