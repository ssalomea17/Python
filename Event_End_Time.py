# if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
print("Current time: "+str(hour)+":"+str(mins))
if dura+mins>60:
    hour=hour+1
    mins=(dura+mins)-60
print("End event: "+str(hour)+":"+str(mins))