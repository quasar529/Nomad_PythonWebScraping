def calculator(a,b,what):
    if(type(a)!=int or type(b)!=int):
        print("Your Input is Wrong. Try Again!")
        a=int(input())
        b=int(input())
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

# a=int(input())
# b=int(input())
# what=input()

result=calculator("10",2,'+')

print(result)
        
