class test:
    def add(self,a,b):
        res=a+b
        return res
    def sub(self,a,b):
        res=a-b
        print("the subtraction is ",res)
    def div(self,a,b):
        res=a/b
        print("the division is ",res)
    def mul(self,a,b):
        res=a*b
        print("the multiplication is ",res)
    
a=int (input("enter first number:"))
b= int(input("enter the second number:"))
t=test()
answer=t.add(a,b)
print("the addition of two numbers are ",answer)



