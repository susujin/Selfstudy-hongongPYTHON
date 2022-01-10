#변수
pi=3.14159
r=10
print("원주율 = ",pi)
print("반지름 = ",r)
print("원의 둘레 = ",2*pi*r)
print("원의 넓이 = ",pi*r*r)

#복합 대입 연산자
string="Hello"
string+="!!"
print(string)

#사용자 입력 input()
name=input("이름 입력> ")
print("제 이름은 ",name,"입니다.")
age=input("나이입력> ")
print(age,"살 입니다.")
print(type(age)) #str 문자

#문자열을 숫자로 변환
str_num=input("숫자를 입력> ")
int_num=int(str_num)
print(type(int_num))