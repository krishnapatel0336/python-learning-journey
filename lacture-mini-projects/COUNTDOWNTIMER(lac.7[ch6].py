#gap=1sec       #for loop       "HAPPY NEW YEAR"
import time

COUNT=int(input("enter the count number:", ))
print("\ncountdown starts now")
for i in range(COUNT,0,-1):
    print(i)
    time.sleep(1)
print("\nHAPPY NEW YEAR 🎆🎆")


