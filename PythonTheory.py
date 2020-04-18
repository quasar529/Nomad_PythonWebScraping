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
# def calculator(a=0,b=0):    #positional argument
#     print(a+b)

# def cal(a,b):               #keyword argument
#     print(a-b)

# cal(b=9, a=10)

# def say_hello_f(name, age):
#     return f"Hello {name} you are {age} years old"
#     #return "Hello"+name+"you are"+ age+ "years old"
# hello=say_hello_f("Jun", "12")

# print (hello)


# def plus(a,b) :
#     if type(b) is int or type(b) is float:  # is , is not
#         return a+b
#     else:
#         return None

# print(plus(12,"10"));

# def age_check(age):
#     print (f"you are {age}")
#     if age<18:
#         print("you can't drink")
#     elif 20<age<25:
#         print("be careful")
#     else:
#         print("enjoy")

# age_check(23)

# days=("mon", "Tue", "wed", "thu")

# for x in days:
#     print(x)

#import
#다른 파일에서 가져올 수도 있음 ex calclator.py 만들고 그 안의 함수 import 가능
# from math import ceil, fsum
# from math import factorial as fac
# print(ceil(1.2))    #사용할 것만 import 하자!
