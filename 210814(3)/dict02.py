# 사전 데이터 관리
# 사전 자료형은 변경 가능한 자료형이다. 따라서 실행중에
# 삽입, 삭제, 수정 등의 편집을 자유롭게 할 수 있다.
# 사전에 데이터를 수정하고나 편집할 때는
# 사전[key] = value 문법을 사용한다.
# 추가한 key가 기존에 존재하는 key라면 value값을 교체해주고
# 그렇지 않다면 key:value 쌍이 사전에 추가된다.
dic = {"boy":"소년","student":"학생","book":"책"}
dic["book"]="서적"
print(dic)

dic["girl"] = "소녀"
print(dic)

# 삭제는 del 명령어를 이용해 할 수 있다.
# del 명령어를 사용하는 경우는 key값을 이용해 key:value를 삭제한다.
del dic["boy"]
print(dic)

# 딕셔너리 자료형의 key만 따로, 혹은 value만 따로 모아서 받고 싶은
# 경우는 keys(), values()를 사용해 얻어올 수 있다.
# 이 경우 key값이나 value값으로만 구성된 유사리스트(list와는 다름)로
# 결과값이 출력되며, items()는 (key, value)형태로 묶은
# 튜플 집합을 출력한다.
# 위의 메서드를 이용해 출력된 자료는 반복문을 이용해 사용할 수 있으나,
# 리스트가 아니기 때문에 편집은 불가능하다.
print("-"*65)
print(dic.keys())
print(dic.values())
print(dic.items())

# key값만 모아서 출력 가능
keylist = dic.keys()
for k in keylist:
    print(k)