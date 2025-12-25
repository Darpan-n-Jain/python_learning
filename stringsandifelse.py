name ="darpan Jain"
print(name)
print(len(name))
print(name[6])#starts form 0
print(name[1:6])#in slicing 1st index is included and 2nd is not
print(name[:6])#form start to 5th indx ie 6th word
print(name[7:])#form 7th index to end of string
print(name[-4:-1]) #starts counting form last taking last char as -1
print(name.endswith("in"))#true if yes else false
print(name.capitalize())#tempory convererts [0] small into capital
name=name.capitalize() #perment
print(name)
print(name.replace("a","A"))#can even replace words
print(name.find("D"))#return index of 1st occ gives -1 if not found
print(name.count("a"))

#if else sytanx:
# if(condition):
#     Code
# elif(condition):
#     code
# else:
#     code
age = int(input("enter your age: "))
if (age >= 18 ):
    print("can vote")
elif(age < 18):
    print("can vote")
else:
    print("end of code")
