'''
syntax :
while(condition):
    block of statement
    increment/decrement

'''
'''
i=1
while (i<=10):
    print("Hi world")
    i+=1 ''' #i=i+1

#wap to get table of given number using while loop
'''
num=int(input ("enter any number:"))
i=1
while(i<=10):
    print(num*i)
    i+=1
    '''
#wap to reverse a number inputnum 123
 #expectedoutput=321
'''
n=int(input ("enter any number:"))
rev=0
while(n>0):
    rem=n%10
    rev =rev*10+rem
    n=n//10
print(rev)
'''

'''
n=123
iteration 1:123>0 T
    rem=123%10=3
    rev=0*10+3=3
    n=n//10=12

iteration 2:12>0 T
    rem=12%10=2
    rev=3*10+2=32
    n=n//10=1

iteration 3:1>0 T
    rem =1%10=1
    rev=32*10+1=321
    n=n//10=0

iteration 4:0>0  F
'''

#wap to check wether the number is palindrome or not .

n=int(input ("enter any number:"))
n1=n
rev=0
while(n>0):
    rem=n%10
    rev =rev*10+rem
    n=n//10
print(rev)

if (rev==n1):
    print("It is palindrome ")
else:
    print("it is not paindrome")


    
    
    
    
    
