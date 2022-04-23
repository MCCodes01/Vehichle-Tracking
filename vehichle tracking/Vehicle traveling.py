# Purpose:    Calculating Traveling Time/Distance
######################################################

speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))

print ("                           ")
print ("{} : {}".format("Hour", "Distance"))

i=1
while(i<hours+1):
   print(i, " ", speed*i);
   i = i+1;
