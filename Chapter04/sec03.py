#범위
a=range(5) #0부터 4까지
b=range(1,5) #1부터 4까지
c=range(1,10,2) #1부터 9까지 2씩 증가

print(a)
print(list(a))
print()

#for문에서 range사용
for i in range(5):
    print(str(i)+"=반복변수")
print()
for i in range(5,10):
    print(str(i)+"=반복변수")
print()
for i in range(0,10,3):
    print(str(i)+"=반복변수")
print()

#리스트와 범위
array=[273,32,103,54,23]
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i,array[i]))
print()

#역반복문
for i in range(4,-1,-1):
    print("현재 반복 변수 : {}".format(i))
print()
for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))
print()

#while반복문
i=0
while i<10:
    print("{}번째 반복입니다.".format(i))
    i+=1
print()

list_test=[1,2,1,2]
value=2

while value in list_test: #2가 제거될때까지 반복
    list_test.remove(value)
print(list_test)
print()

#시간기반반복
import time
number=0

target_tick=time.time()+5
while time.time()<target_tick:
    number+=1
print("5초 동안 {}번 반복했습니다.".format(number))
print()

#while-break,continue
i=0
while True:
    print("{}번쩨 반복문입니다.".format(i))
    i+=1
    input_text=input(">종료하시겠습니까?(y):")
    if input_text in ["y","Y"]:
        print("종료합니다.")
        break
print()

numbers=[5,3,67,2,32]
for number in numbers:
    if number<10:
        continue
    print(number)
print()

