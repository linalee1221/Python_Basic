# 문자열 포맷팅은 가변 출력 자료와 고정 출력자료를 구분해서
# 출력 양식을 지정해두고 가변 출력 자료만 교체하는 출력방식이다.
# 문자열 내부에 포멧팅 문자를 이용해서 가변 출력 자료 위치를 지정하며
# %d는 정수, %f는 실수, %s는 문자열, %h는 16진수, %o는 8진수 등
# 여러가지 포맷팅 문자를 활용할 수 있다.
# 만약 %를 문자로서 사용하고 싶다면 %%와 같이 2번 연달아 쓴다.
from setuptools.command.test import ScanningLoader

tvxq = 5
print("동방신기는 " + str(tvxq) + "명!")
print("동방신기는", tvxq, "명!")
print("동방신기는 %d명!" % tvxq)

# %를 문자열로 쓰고싶다면 %%를 사용
percent=97
print("오늘 학습 진도율은 %d%%"%percent)

# 만약 포맷팅이 여럿인 경우는 % 뒤에 나열할 자료를 ()로 감싸준다.
month=6
day=6
anni = "현충일"
print("%d월 %d일은 %s" % (month, day, anni))