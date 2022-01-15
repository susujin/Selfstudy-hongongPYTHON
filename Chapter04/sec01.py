#리스트
list_a=[1,2,3]
list_b=[4,5,6]

print("list_a = ",list_a)
print("list_b = ",list_b)
print("list_a + lisb_b = ",list_a+list_b)
print("list_a * 3 = ",list_a*3)
print("list_a 길이 = ",len(list_a))
print()

#리스트 요소 추가
list_a=[1,2,3]
list_a.append(4)
list_a.append(5)
print("list_a = ",list_a)
list_a.insert(0,10)
print("list_a = ",list_a)
print()

#리스트 요소 제거
list_a=[0,1,2,3,4,5]
del list_a[1] #1번 인덱스 제거
print("list_a = ",list_a) #0 2 3 4 5
list_a.pop(2) #2번 인덱스 제거
print("list_a = ",list_a) #0 2 4 5
print()

list_a=[0,1,2,3,4,5]
del list_a[3:6] # 인덱스 3~5삭제
print("list_a = ",list_a) #0 1 2 6
print()

list_c=[1,2,1,2]
list_c.remove(2) #값을 제거. 2제거. 맨 앞에 있는 2제거
print("list_c = ",list_c)
print()

#전체제거
list_d=[3,5,2,16,63]
print("list_d = ",list_d)
list_d.clear()
print("list_d = ",list_d)
print()

#리스트 내부에 있는지 확인 in/not in
list_e=[3,7,2,8,5,3,6,4]
print(4 in list_e)
print(9 in list_e)
print(4 not in list_e)
print(9 not in list_e)
print()

#for 반복문
array=[285,346,164,52,65]
for element in array:
    print(element)
print()

#마무리 연습문제 02
numbers=[273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number>=100:
        print("- 100 이상의 수: ",number)
print()

#마무리 연습문제 03
numbers=[273,103,5,32,65,9,72,800,99]
for a in numbers:
    if a%2==0:
        print(a,"는 짝수입니다.")
    else:
        print(a,"는 홀수입니다.")

for b in numbers:
    print(b,"는 ",len(str(b)),"자릿수입니다.")
print()

#마무리 연습문제 04
list_of_list=[
    [1,2,3],
    [4,5,6,7],
    [8,9],
]
for l in list_of_list:
    for element in l:
        print(element)
print()

#마무리 연습문제 05
numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]

for number in numbers:
    output[(number+2)%3].append(number)
print(output)