# 아래 보이는 변수 dan에 숫자를 입력하면
# 1~9까지 곱해 결과를 얻어내는 구구단 로직을 작성해라.
dan = int(input("구구단 단수를 입력해주세요"))
for hang in range(1,10):
    print(str(dan) + " * " + str(hang) + " = " + str(dan * hang))


        