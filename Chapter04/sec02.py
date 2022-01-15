#딕셔너리
dict_a={
    "name":"캐리비안의 해적",
    "type":"액션",
}
print(dict_a["name"])
print(dict_a["type"])
print()

dict_a["name"]="반지의 제왕:반지 원정대"
print(dict_a["name"])
dict_a["type"]="판타지"
print(dict_a["type"])

#딕셔너리 값 추가, 제거
dict_a["time"]=228
dict_a["score"]=9.84
print(dict_a)
del dict_a["time"]
print(dict_a)
print()

#딕셔너리 내부에 키가 있는지 확인하기
dict_b={
    "name":"떡볶이",
    "type":"분식",
    "ingredient":["떡","파","소스","어묵"]
}

key=input(">접근하고자 하는 키: ")
if key in dict_b:
    print(dict_b[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()

#for 반복문
dict_c={
    "name":"배스킨라빈스",
    "type":"아이스크림",
    "flavor":["엄마는외계인","민트초콜릿칩","아몬드봉봉","체리쥬빌레","초코나무숲","자모카 아몬드 훠지"],
    "size":["파인트","쿼터","패밀리","하프갤런"]
}

for key in dict_c:
    print(key,":",dict_c[key])
print()

#마무리 연습문제 02
pets=[
    {"name":"구름","age":5},
    {"name":"초코","age":3},
    {"name":"아지","age":1},
    {"name":"호랑이","age":1},
]

print("#우리 동네 애완 동물들")
for a in pets:
    print(a["name"],str(a["age"])+"살")
print()

#마무리 연습문제 03
numbers=[1,2,4,3,6,6,4,3,7,5,3,7,8,8,8,6,5,4,3,3,5,6,7,4,3,2,1,2]
counter={}

for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1

print(counter)
print()

#마무리 연습문제 04
character={
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for f in character[key]:
            print(f,":",character[key][f])
    elif type(character[key]) is list:
        for i in character[key]:
            print(key,":",i)
    else:
        print(key,":",character[key])