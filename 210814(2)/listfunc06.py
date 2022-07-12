# .sort()는 내부 요소를 크기가 작을수록 0번에 가깝게 재배치 해준다.
# .reserve()는 내부 요소를 인덱스번호 역순으로 재배치 해준다.
score = [88,95,70,100,99]
score.sort() #오름차순 정렬
print(score)
score.reverse() #sort사용 후 reverse사용시 큰 숫자가 왼쪽으로
print(score)

# .sort(reverse=True)로 정렬시 내림차순 정렬(큰숫자->작은숫자)
score=[24,35,22,13,55,79]
score.sort(reverse=True) #내림차순 실행
print(score)

