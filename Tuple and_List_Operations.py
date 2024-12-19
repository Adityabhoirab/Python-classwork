t1=("aditya",35,78,"O grade")
print (type(t1))
print(t1)

#tuple slicing 
print(t1[1:])
print(t1[:3])
print(t1[1:3])

#find length of the tuple

print("the length of the tuple is :",len(t1))

#you can alos given negative indexing.
print(t1[-2])
print(t1[-1])

#note:
#list is a collection which is ordered and changeable
# list allows duplicate members.
#tuple is a collection which is ordered and unchangeable
#tuple allows duplicate members


t2=list(t1)
print(t2)

t2[2]="a in sports"
print(t2)

for i in t2:
    print (i)
