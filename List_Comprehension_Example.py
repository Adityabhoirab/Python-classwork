'''
to present list in concise and easy way we use list comprehension 
as size of the code is less, performance will be increased
'''
marks= [20,35,50,78,40]
new_marks=[]  #empty list 
for x in marks :
    new_marks.append(x+2)
print (new_marks)

#code using list comprehension
marks=[20,35,50,78,40]
new_marks=[x+2 for x in marks ]
print(new_marks)
