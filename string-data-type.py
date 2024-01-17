myString = "This is a string."
print(myString)
print(myString + " is of the data type " + str(type(myString)))
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
name = input("What is your name? ")
print("Name",name)
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
myVal=3
print("{}, you like a {} {} {}!".format(name,color,myVal,animal))