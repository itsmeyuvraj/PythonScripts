import pickle


file = open("sum.txt",mode="w")
numbers=[]
number = []
first_num = input("Enter first number : ")
last_num= input("Enter second number :")


pickle.dump()
# file.write(first_num)
# # file.write("\n")
# file.write(last_num)
# file.flush()
# file.close()

def summ(number=[]):
    return int(sum(numbers))

files = open("sum.txt",mode="r")

for n in range(0,3):
#    numbers.append(files.read(n))
   numbers.append(files.read(n))

# print(type(numbers[1]))

# listt= []

# for n in numbers:
#     number= int(numbers.values())

    


# summ(number)

for n in range(0,3):

    numberss[n]= int(files.read(n))

    # print(type(numbers[n]))

# numbersss = list(map(int, numbers))


summ(numberss)


