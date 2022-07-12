# 1. 회원의 이름과 성별 그리고 나이를 입력 받기
# 2. 이름 변수는 name, 성별은 gender, 나이는 age
# 3. 입력받은 값을 통해 회원의 이름과 성별과 나이와 출생년도를 출력
name = input("이름: ")
gender = input("성별: ")
age = int(input("나이: "))
year = 2021 - age + 1
print("--------------------")
print("이름:", name)
print("성별:", gender)
print("나이:", age)
print("출생년도:", year)