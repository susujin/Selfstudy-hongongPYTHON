#format() 함수
string_a="{}".format(10)
print(string_a)
print(type(string_a))
print()

format_a="{}만원".format(5)
format_b="{} {} {}".format(10,20,30)
print(format_a)
print(format_b)
print()

output_a="{:d}".format(23)
output_b="{:5d}".format(23) #앞에 5칸 비우기
output_c="{:10d}".format(23) #앞에 10칸 비우기
output_d="{:05d}".format(23) #앞에 5칸을 0으로 채우기
output_e="{:010d}".format(23) #앞에 10칸을 0으로 채우기
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)
print()

output_f="{:+d}".format(55) #양수
output_g="{:+d}".format(-55) #음수
output_h="{: d}".format(55) #기호공백 양수
output_i="{: d}".format(-55) #기호공백 음수
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print()

output_j="{:+5d}".format(83) #기호 뒤로 밀기 양수
output_k="{:+5d}".format(-83) #기호 뒤로 밀기 음수
output_l="{:=+5d}".format(83) #기호 앞으로 밀기 양수
output_m="{:=+5d}".format(-83) #기호 앞으로 밀기 음수
output_n="{:+05d}".format(83) #0으로 채우기 양수
output_o="{:+05d}".format(-83) #0으로 채우기 음수
print(output_j)
print(output_k)
print(output_l)
print(output_m)
print(output_n)
print(output_o)
print()

out_a="{:f}".format(52.493)
out_b="{:15f}".format(52.493) #15칸 비우기
out_c="{:+15f}".format(52.493) #15칸 비우고 부호
out_d="{:+015f}".format(52.493) #15칸 빈 곳에 0채우고 부호
print(out_a)
print(out_b)
print(out_c)
print(out_d)
print()

out_e="{:15.3f}".format(75.342)
out_f="{:15.2f}".format(75.342)
print(out_e)
print(out_f)
print()

out_g="{:g}".format(34.0)
print(out_g)
print()

#upper() lower()
hi="Hello~ Python!"
print(hi.upper())
print(hi.lower())
print()

#strip() 공백제거
abc='''
        안녕하세요
공백을 제거합니다
'''
print(abc)
print(abc.strip()) #양옆 공백 제거
print()

#문자열 구성 파악하기 is??()
print("Hello".isalpha()) #알파벳으로만 구성되어 있는지
print("hello3".isalnum()) #알파벳 또는 숫자로만 구성되어 있는지
print("32.543".isdecimal()) #정수 형태인지
print()

#문자열 찾기 find() rfind()
a="안녕하세요. 안녕??"
print(a.find("안녕"))
print(a.rfind("안녕"))
print()

#in
print("안녕"in"안녕하세요")
print()

#문자열 자르기 split()
b="10 20 30 40 50".split()
print(b)

#마무리 연습문제 03
num1=input("> 1번째 숫자 : ")
num2=input("> 2번째 숫자 : ")
print()
num1=int(num1)
num2=int(num2)
print("{} + {} = {}".format(num1,num2,num1+num2))
print()