#리스트에 적용가능한 함수
numbers=[103,405,43,6,3,50]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

#reversed()로 리스트 뒤집기
list_a=[1,2,3,4,5]
list_reversed=reversed(list_a)
print(list(list_a))
print(list(list_reversed))
print()

#enumertae()
ex_list=["a","b","c"]
print("단순출력")
print(ex_list)
print()

print("enumerate() 적용출력")
print(enumerate(ex_list))
print()
print(list(enumerate(ex_list)))
print()

print("반복문 조합")
for i, value in enumerate(ex_list):
    print("{}번째 요소는 {}입니다".format(i,value))
print()

#items()
ex_dict={
    "키a":"값a",
    "키b":"값b",
    "키c":"값c"
}
print("items(): ",ex_dict.items())
print()

print("반복문 조합")
for key, element in ex_dict.items():
    print("dictionary[{}] = {}".format(key,element))
print()

#반복문사용 리스트 생성
array=[]
for i in range(0,20,2):
    array.append(i*i)
print(array)
print()

#리스트 안에 for문
array=[i*i for i in range(0,20,2)]
print(array)
print()

#조건을 활용한 리스트 내포
array=["사과","바나나","복숭아","포도","딸기","체리"]
output=[fruit for fruit in array if fruit != "초콜릿"] #리스트이름=[표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
print(output)

#마무리 연습문제 02
output=[i for i in range(1,101) if "{:b}".format(i).count("0")==1]

for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
print("합계: ",sum(output))