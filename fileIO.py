a=open("python_learning/demo.txt", "w")#open-.to open file name,mode
#r->reading,w->writing(overwrites privous data),x->create new file and open in w,a->to append data in file,b->binary mode,t->txt mode

# data = a.read()
# print(data)
# d=a.read(5)
# print(d)
# l1=a.readline()
# print(l1)
a.write("test")
with open("info.txt","a+") as i: #ANOTHER WAY TO APEN A FILE aoto closes the file
    i.write("hi i am darpan")

import os
os.remove("info.txt")