switch = {
   
       "Monday": 1,
       "Tuesday": 2,
       "Wednesday": 3,
       "Thrusday": 4,
       "Friday" : 5,
       "Saturday" : 6,
       "Sunday" : 7
       
       }


def converttodays(days):

    return switch.get(days)


print(converttodays("Tuesday"))
print(converttodays("Wednesday"))
