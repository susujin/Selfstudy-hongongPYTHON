#함수 기본
def print_3_times():
    print("hi")
    print("hi")
    print("hi")

print_3_times()
print()

#매개변수 기본
def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안녕",5)
print()

#가변 매개변수
def print_n_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,"안녕","올해도","파이팅")
print()

#기본 매개변수
def print_n_times(value,n=2):
    for i in range(n):
        print(value)
print_n_times("기본매개변수")
print()

#기본매개변수가 가변매개변수보다 앞에 올때 #오류ㅋㅋ
# def print_n_times(n=2,*value):
#     for i in range(n):
#         for value in value:
#             print(value)
#         print()
# print_n_times("hi","funfun","programing")

#가변매개변수가 기본매개변수보다 앞에 올때
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("apple","is","red",3) #2번출력, 3은 같이 2번 출력됨.
print()

#키워드 매개변수
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("peach","is","pink?",n=3) #3번출력, 매개변수 이름을 지정해서 n=3으로 입력했으므로 3번 출력됨
print()

#여러 함수 호출 형태
def test(a,b=10,c=100):
    print(a+b+c)
#기본
test(10,20,30)
#키워드로 모두 지정
test(a=10,b=200,c=300)
#키워드로 순서 상관 없이 지정
test(c=10,a=100,b=200)
#키워드로 일부만 지정
test(10,c=200)
print()

#리턴
def return_test():
    print("a위치입니다.")
    return
    print("b입니다.") #절대 실행xxx

return_test()
print()

def return_test():
    return 100
value=return_test()
print(value)
print()

def return_test():
    return
value=return_test()
print(value)
print()

#기본 함수 활용
def sum_all(start,end):
    output=0
    for i in range(start,end+1):
        output+=i
    return output
print("0 to 100 : ", sum_all(0,100))
print("50 to 100 : ", sum_all(50,100))
print()

def sum_all(start=0,end=100,step=1):
    output=0
    for i in range(start,end+1,step):
        output+=i
    return output
print("a.",sum_all(0,100,10))
print("b.",sum_all(end=100))
print("c.",sum_all(end=100,step=2))