theinput = input("pleas enter the time:(the divider must be dots)")
hour =int(theinput[0:2] ) * 60
min =  int(theinput[3:5])
sec = int(theinput[6:8])
sec = (hour + min) * 60 + sec
print(sec)

