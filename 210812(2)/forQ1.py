# 1부터 1000까지의 숫자 중 n의 배수의 합을 구할 수 있도록
# for in문을 사용해서 코드를 작성해주세요.
# n의 배수의 값은 input()을 이용해 입력받습니다.

sum = 0
n = int(input("배수를 입력해주세요: "))
for number in range(0, 1001, n):
    sum += number
print("총합은", sum, "입니다.")