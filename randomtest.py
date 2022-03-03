import random
import pickle



word_list = []

f= open("paragraph.txt", mode="r")
for line in f:
        word_list.extend(line.split())     #write all the words to a list from a text file

print(word_list)
    

randomobj= random.Random()
word = randomobj.choice(word_list)   #choose a random index from the list



outfile = open("voterID.txt",mode="wb")  #serialize the list object to a file for persistent 
pickle.dump(word_list, outfile)
outfile.close()


infile= open("voterID.txt",mode="rb")     #read the list 

list2 = pickle.load(infile)
print(word)






