# "20180819-134709.jpg"라는 파일 경로가 있을 때
# print("촬영날짜 : " ....)
# print("촬영시간 : " ....)
# print("확장자 : " ....)
# 정보를 따로따로 아래와 같이 출력해보기.
# 촬영 날짜: 08월 19일
# 촬영 시간: 13시 47분 09초
# 확장자: jpg
file = "20180819-134709.jpg"
print("촬영 날짜:",file[4:6]+"월",file[6:8]+"일")
print("촬영 시간:",file[9:11]+"시",file[11:13]+"분",file[13:15]+"초")
print("확장자:",file[-3:])
