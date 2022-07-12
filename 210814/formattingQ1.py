# ssn변수에 주민번호를 문자열로 입력받아 ex)"971216-1209321"
# 여기서 성별과 출생년도를 추출한 후 포맷팅을 사용하여
# "xx년생 남자or여자"라는 결과를 출력하세요.
ssn=input("주민번호를 입력하세요: ")
birth = ssn[0:2]
if (int(ssn[7]) % 2 == 1):
    gender = "남자"
else:
    gender = "여자"
print("%s년생%s" % (birth, gender))