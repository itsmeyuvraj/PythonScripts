list1 = [2,3,4,5,6,7]
list2 = [2,3,4,5,6,7]

tuple1 = (1,2,3,4,5)
tuple2 = (1,2,3,4,5)

dict1 = {"1": 1,"2": 2,"3": 3}
dict2 = {"1": 2,"2": 8,"3": 9}


print("List --> ",list1 + list2)
print("Tuple --> ", tuple1 + tuple2)
# print("Dict --> ",sum(dict1.values() + dict2.values()))
print("Dict --> ",dict2.update(dict1))

dict1=dict2.update(dict1)
print(dict1)






