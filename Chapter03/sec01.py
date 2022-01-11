#불린 불리언
print("바지"=="치마") #false
print("바지"!="치마") #true
print(10<100) #true
print(10>100) #false
print(10<=100) #true
print(10>=100) #false
print()

print(not True) #false
print(not False) #true
print()

print(True and True) #true
print(True and False) #false
print(True or True) #true
print(True or False) #true
print()

#if조건문
number=input("숫자를 입력하세요 > ")
number=int(number)

if number>0:
    print("양수")

if number<0:
    print("음수")

if number==0:
    print("0")
print()

#날짜와 시간
import datetime
now=datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
print()

if now.hour<12:
    print("현재 시각은 {}시이므로 오전입니다.".format(now.hour))
if now.hour>=12:
    print("현재 시각은 {}시이므로 오후입니다.".format(now.hour))
print()

#짝홀 구분 if
num=input("숫자를 입력하세요 > ")
last_ch=num[-1]

# if last_ch==0 or last_ch==2 or last_ch==4\
#     or last_ch==6 or last_ch==8:
#     print("짝수입니다.")
# if last_ch==1 or last_ch==3 or last_ch==5\
#     or last_ch==7 or last_ch==9:
#     print("홀수입니다.")
# print()

#여기서는 문자로
if last_ch in "02468":
    print("짝수입니다.")
if last_ch in "13579":
    print("홀수입니다.")
print()

#여기서는 숫자로
last_num=int(last_ch)
if last_num%2==0:
    print("짝수입니다.")
if last_num%2==1:
    print("홀수입니다.")
print()
print("=============================================")

#마무리 연습문제 04
a=int(input("> 1번째 숫자 : "))
b=int(input("> 2번째 숫자 : "))
print()

if a>b:
    print("처음 입력했던 {}가 {}보다 더 큽니다.".format(a,b))
if b>a:
    print("두 번째로 입력했던 {}가 {}보다 더 큽니다.".format(b,a))