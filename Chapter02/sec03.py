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

#마무리 연습문제 04
str_input1=input("숫자 입력> ")
num_input1=float(str_input1)
print()
print(num_input1,"inch")
print((num_input1*2.54),"cm")

#마무리 연습문제 05
str_input2=input("원의 반지름 입력> ")
num_input2=float(str_input2)
print()
print("반지름: ",num_input2)
print("둘레: ",2*3.14*num_input2)
print("넓이: ",3.14*num_input2**2) # '**'는 제곱

#마무리 연습문제 06
a=input("문자열 입력> ")
b=input("문자열 입력> ")

print(a,b)
change=a
a=b
b=change
print(a,b)