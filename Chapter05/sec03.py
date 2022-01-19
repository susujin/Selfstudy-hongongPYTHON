#튜플
tuple_test=(10,20,30)
print(tuple_test[0])
print(tuple_test[1])
print(tuple_test[2])
print()

#괄호 없는 튜플
tuple_test=10,20,30,40
print(tuple_test)
print(type(tuple_test))
print()

#변수값 교환 튜플
a,b=10,20
print("교환전")
print("a: ",a)
print("b: ",b)
a,b=b,a
print("교환후")
print("a: ",a)
print("b: ",b)
print()

#튜플과 함수
def test():
    return (10,20)
a,b=test()
print("a: ",a)
print("b: ",b)
print()

#함수의 매개 변수로 함수 전달
def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print("안녕하세요")

call_10_times(print_hello)
print()

#map()와 filter()
#두함수 모두 첫번째 매개변수에는 함수, 두번째 매개변수에는 리스트를 넣는다.
def power(item):
    return item*item
def uner_3(item):
    return item<3

list_input_a=[1,2,3,4,5]

output_a=map(power,list_input_a)
print("map()실행")
print("map(power,list_input_a) : ",output_a)
print("map(power,list_input_a) : ",list(output_a))
print()
output_b=filter(uner_3,list_input_a)
print("filter()실행")
print("filter(uner_3,list_input_a) : ",output_b)
print("filter(uner_3,list_input_a) : ",list(output_b))
print()

#람다
power=lambda x:x*x
uner_3=lambda x:x<3

list_input=[1,2,3,4,5]
output_a=map(power,list_input_a)
print("map(power,list_input_a) : ",output_a)
print("map(power,list_input_a) : ",list(output_a))
print()
output_b=filter(uner_3,list_input_a)
print("filter()실행")
print("filter(uner_3,list_input_a) : ",output_b)
print("filter(uner_3,list_input_a) : ",list(output_b))
print()

#인라인 람다
list_input=[1,2,3,4,5]

output_a=map(lambda x:x*x,list_input)
print("map(power,list_input_a) : ",output_a)
print("map(power,list_input_a) : ",list(output_a))
print()
output_b=filter(lambda x:x<3,list_input_a)
print("filter()실행")
print("filter(uner_3,list_input_a) : ",output_b)
print("filter(uner_3,list_input_a) : ",list(output_b))
print()

#마무리 연습문제 01
numbers=[1,2,3,4,5,6]
print("::".join(map(str,numbers)))
print()

#마무리 연습문제 02
numbers=list(range(1,10+1))

print("홀수만 추출")
print(list(filter(lambda x:x%2==1,numbers)))
print()

print("3이상 7미만 추출")
print(list(filter(lambda x:x>=3 and x<7,numbers)))
print()

print("제곱해서 50미만 추출")
print(list(filter(lambda x:x**2<50,numbers)))
print()