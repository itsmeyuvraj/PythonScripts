

def average(a=[]):
    print(sum(a)/len(a))


# average([23,44,55,66,666])
# average([10,34,33,45,66,77,566,666,55,66656])

n= int(input("Enter the number of marks you want to enter: "))
marks = []
for n in range(0,n):
    
    markss= int(input("Enter the marks: "))
    marks.append(markss)

print(marks)

average(marks)

