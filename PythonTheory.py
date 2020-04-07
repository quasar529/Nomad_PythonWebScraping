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
def calculator(a=0,b=0):
    print(a+b)

calculator(4,5)