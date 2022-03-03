import pickle

num= []


def summ(num):
    print(sum(num))


number = [0,0,0]

number[1]= int(input("Enter first number :"))
number[2]= int(input("Enter second number :"))



outputfile = open("sumfile.txt",mode="wb")


pickle.dump(number, outputfile)   #writing into a file as a serialized object  
outputfile.close()

infile = open("sumfile.txt",mode="rb")    #reading from a file as a serialized object
numbers = pickle.load(infile)
infile.close()

print(summ(numbers))



