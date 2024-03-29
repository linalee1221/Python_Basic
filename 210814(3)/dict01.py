# 딕셔너리는 사전이라고도 하며 key, value 쌍으로 자료를 저장한다.
# {}를 이용해 저장하며 key:value, key2:value2 ...와 같이
# 콜론을 이용해 key와 value를 매칭시켜 저장한다.
# 딕셔너리는 인덱스 번호로 내부 자료 조회가 불가능하다.
dic = {"멍멍이":"홍길동", "야옹이":"강감찬", "메뚜기":"장보고"}
print(type(dic))
print(dic)

# 사전에서 사용하는 key값은 중복값을 가질 수 없고
# 변경이 가능한 요소(리스트, 일반 변수 등...)은 올 수 없다.
# 반면에 value값은 중복된 요소가 들어와도 상관이 없으며
# 변경 가능한 요소 및 불가능한 요소가 모두 올 수 있다.
# 사전에서 자료를 조회할 때는 index값 대신 key값을 사용한다.
# key값으로 value를 얻을 수는 있지만 반대는 불가능하다.
print(dic["멍멍이"])
print(dic["야옹이"])

# 검색하는 키가 사전 내부에 존재하지 않으면 에러를 발생시킨다.
# print(dic["귀뚜라미"])
# .get()을 사용하면 없다고 안내만 하고 에러는 발생하지 않는다.
print(dic.get("귀뚜라미"))
# none대신 없을때 출력할 멘트를 지정할 수도 있다.
print(dic.get("귀뚜라미", "없는 자료입니다."))
print(dic.get("메뚜기"))

# 딕셔너리 자료형은 무조건 key값 기반으로 움직이기 때문에
# in, not in 키워드 조회시 key값을 기준으로 결과가 출력된다.
if "강감찬" in dic:
    print("사전에 있는 단어입니다.")
else:
    print("사전에 없는 단어입니다.")
    
