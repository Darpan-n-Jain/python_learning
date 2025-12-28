dar={
    "name" : "darpan", #key:value, (, is nessery )
    "surname" : "jain",
    "age" : 19
}
print(dar)
dar["name"]="Darpan"#overwrite
print(dar)
acd ={
    "name":"darpan",
    "sub" :{
        "math":50,
        "phy":60,
        "chem":80,
    },
    "batch":"s"
}
print(acd)
print(acd["sub"])
print(acd["sub"]["chem"])
print(dar.keys())#prints all keys in dictionary
print(acd.keys())#prints all keys in dictionary not including nested
print(dar.values())#prints all values in dictionary
print(dar.items())#stores pair of key and values as tupel
print(dar.get("name"))#retutns none if key not found no error 
dar.update({"coll":"iiitn"})#add key value pair to dictionary
print(dar)

#sets(are like tupel but cant reapet element) are cant store list and dictionary
num={0,5,6,"darpan","jain",5,4,0,"darpan"}#ingnore reapting values and is unordred
print(type(num))
print(num)
num.add(7)#adds element in set
print(num)
num.remove("darpan")#removes an elements gives etror if element dosent exist in set
print(num)
num.pop()#removes random value form set
print(num)
num.clear()#empty set
print(num)
num2={0,8,6,1}
print(num.union(num2))#union of 2 sets like in math
print(num.intersection(num2))#prints common values of both set