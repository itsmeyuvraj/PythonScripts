marks = {

    "Yuvraj" : 100,
    "Rajdeep" : 200,
    "Shreyas" : 300,
    "Sanket" :400,
    "Amit" : 500

}


def getmarks(name):
    return marks.get(name)


i = input("Whose marks you want to view? ")
print("His marks is :",getmarks(i))