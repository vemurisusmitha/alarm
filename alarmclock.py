import datetime
from winsound import PlaySound  
from playsound import playsound

hours =int(input("enter hours:"))
minutes=int(input("enter minutes:"))
meridiem=input("am / pm :")
if meridiem=="pm": 
    hours=hours+12
    while True: 
        if hours==datetime.datetime.now().hour and minutes==datetime.datetime.now().minute:
            print("alarm is ringing")
            playsound('levi-oi.mp3')
            
            break 