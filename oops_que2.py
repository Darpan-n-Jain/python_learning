with open("q.txt","w") as f:
    f.write("Hi everyone\n we are learning file i/o \n using java")
with open("q.txt","r") as f:
    data=f.read()
    d=data.replace("java","python")
with open("q.txt","w") as f:
    f.write(d)
w="learning"
if data.find(w) != 1:
    print("word NOT found")
else:
        print("word found")