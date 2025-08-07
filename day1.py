Mylist=["apple","banana","cherry","orange"]
Mylist[1:2]=["war","war1"]
print(Mylist)

Mylist=["apple","banana","cherry","orange"]
Mylist[1:3]=["watermelon"]
print(Mylist)

Mylist=["apple","banana","cherry","orange"]
Mylist.insert(2,"watermelonn")
print(Mylist)

Mylist=["apple","banana","cherry","orange"]
Myfavourite=["banana","graphs","mango"]
Mylist.extend(Myfavourite)
print(Mylist)

Mylist=["apple","banana","cherry","orange"]
del Mylist[2]
print(Mylist) 

Mylist=["apple","banana","cherry","orange"]
for i in Mylist:
   print(i)

Mylist=["apple","banana","cherry","orange"]
for i in range(len(Mylist)):
    print(Mylist[i]) 

Mylist=["apple","banana","cherry","orange"]
i=0
while i < len(Mylist):
    print(Mylist[i])
    i=i+1

Mylist=["apple","banana","cherry","orange"]
newlist=[]
for x in Mylist:
    if "c" in x:
        newlist.append(x)
print(newlist)

Mylist=["apple","banana","cherry","orange","graphs"]
Mylist.sort()
print(Mylist)

thisdict ={
"brand":"ford",
"model":"Mustang",
"year":1964  
}
print(thisdict["year"]) 

thisdict ={
"brand":"ford",
"model":"Mustang",
"year":1964,
"name":"Vinod"
}
print(len(thisdict))

day = 4
if day in [1,2,3,4,5]:
    print("Today is weekday")
elif day in [6,7]:
    print("I love weekends")
