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

#마무리 연습문제 02
key_list=["name","hp","mp","level"]
value_list=["기사",200,30,5]
character={}

for i in range(0,len(key_list)):
    character[key_list[i]]=value_list[i]

print(character)
print()

#마무리 연습문제 03
limit=10000
i=1

sum_value=0
while sum_value<limit:
    sum_value+=i
    i+=1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))
print()

#마무리 연습문제 04
max_value=0
a=0
b=0

for i in range(1,100):
    j=100-i

    if i*j>max_value:
        max_value=i*j
        a=i
        b=j

print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))
print()