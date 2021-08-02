#The predefinied function input("<string_parameter>") receives a parameter string
#So, if you need to get a int data, you have to realize the conversion 
#Something like this...

age=input("What's your age? ")
age=int(age)
nextyearage=age+1
nextyearage=str(nextyearage)
print("And when you turn " +(nextyearage)+ " ??")

#A most simple alternative...
#age=int(input("What's your age? "))
#nextyearage=str(age+1)
#print("And when you turn "+nextyearage+ " ?")