# 문제
user = {"kim1234":"kkk1234",
        "lee4567":"lll4567",
        "park9876":"ppp9876"}
# user에 내장된 key:value는 아이디:비밀번호이다.
# input()을 이용해 id변수에는 id를, pw변수에는 비밀번호를 입력받아
# id와 pw가 모두 user내부에 입력된 쌍과 일치할때만
# id님 로그인을 환영합니다, 그렇지 않은 경우
# 없는 아이디 입력시 "아이디가 없습니다", 아이디는 있는데
# 비밀번호가 틀렸을 경우는 "비밀번호가 다릅니다"라고 출력해라.

print("\n아이디와 비밀번호를 입력하세요.")
id = input("아이디: ")
pw = input("비밀번호: ")

for id in user:
    if pw == user[id]:
        print(id + "님 로그인을 환영합니다.")
    else:
        print("비밀번호가 다릅니다.")
else:
    print("존재하지 않는 회원입니다.")