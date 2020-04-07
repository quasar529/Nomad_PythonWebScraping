# 파이썬은 샵이 주석이다
# 세미콜론 필요 없다
'''작은따옴표 3개도 주석'''
# type : int, float, bool, str, none
# sequence type : list, tuple

# list : list=[..] 
# list 는 mutable sequence (변경가능)

# 배열에 어떤 원소 있나 확인 가능 ex) print("Mon" in days)= True/False
# tuple : tuple=(..)
# dictionary : class 와 유사
# 함수 만들기 : def sth():  ...
# 중괄호 없이 들여쓰기로 구분
# 들여쓰기 해야 body 안에 포함됨

# default argument 사용 가능

# return 후 함수 종료, 즉 2번 return 불기
def calculator(a=0,b=0):    #positional argument
    print(a+b)

def cal(a,b):               #keyword argument
    print(a-b)

cal(b=9, a=10)

def say_hello_f(name, age):
    return f"Hello {name} you are {age} years old"
    #return "Hello"+name+"you are"+ age+ "years old"
hello=say_hello_f("Jun", "12")

print (hello)