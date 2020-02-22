import datetime

imer= input("Insert a target date: ")
D= imer.split("/")
for i in range(0, len(D)): 
    D[i] = int(D[i]) 
day= D[0]
month= D[1]
year= D[2]

delta = datetime.datetime(year, month, day) - datetime.datetime.now()
print(delta.days, "days")
print(delta.seconds//3600, "hours")
sec= delta.seconds - ((delta.seconds//3600)*3600)
print(sec, "seconds")

if (month== 2):
 print("Ο",month,"ος μήνας του χρόνου έχει 28 μέρες")

elif (month== "1" or "3" or "5" or "7" or "8" or "10" or "12"):
 print("Ο",month,"ος μήνας του χρόνου έχει 31 μέρες")

elif (month== "4" or "6" or "9" or "11"):
 print("Ο",month,"ος μήνας του χρόνου έχει 30 μέρες")
