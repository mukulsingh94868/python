import time
s=input("what is your name")
currentTime = time.strftime('%H:%M')   

if currentTime.hour < 12 :
     print('Good morning')
if currentTime.hour > 12 :
     print('Good afternoon')
if currentTime.hour > 6 :
     print('Good evening')
