#list are arrays in wgich we can save diff type of data
#sicing is same as strings
marks = ["darpan",52.4,94,96.8,87,20,55.5,99]
print(marks)
print(marks[5])
print(marks[1:6])#in slicing 1st index is included and 2nd is not
print(marks[:6])#form start to 5th indx ie 6th word
print(marks[7:])#form 7th index to end of string
print(marks[-4:-1]) #starts counting form last taking last char as -1
marks.append("check")#adds to end of list
print(marks)
num=[1,4,10,5,8,18,20,45,62,70,0]
print(num)
num.sort()#acc sort
print(num)
num.sort(reverse=True)#for dec sort
print(num)
num.reverse()#reverse list
print(num)
marks.reverse()
print(marks)
marks.insert(0,"darpan")#insret at nth index
print(marks)
marks.remove(87)#removes 1st element with sa,e value
print(marks)
marks.pop(0)#removes element at given index
print(marks)
#tupel are same as list but we cant chage its vale or add another element in it 
tup =(0,5,10,4)
print(tup.index(4))#gives frist index where element in equal
print(tup.count(4))#coun how many time element occ
