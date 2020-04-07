def calculator(a,b,what):
    if(type(a)!=int or type(b)!=int):
        print("Your Input is Wrong. Try Again!")
        a=input()
        b=input()
        what=input()
        calculator(a,b,input)
    
    if what=='+':
        return (a+b)
    elif what=='-':
        return (a-b)
    elif what=='*':
        return (a*b)
    elif what=='/':
        return (a/b)
    elif what=='%':
        return (a%b)
    elif what=='^':
        return pow(a,b)

a=input()
b=input()
what=input()

result=calculator(a,b,what)

print(result)
        
