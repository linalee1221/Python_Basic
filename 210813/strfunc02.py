# 특정 문자가 특정 문자열 내부에 포함되어 있는지 여부는
# in, not in 키워드로 조회 할 수 있다.
# in 키워드는 "있는지" 여부를 질문하는 것이며 있으면 True, 없으면
# False이다. 반면 not in 키워드는 "없는지" 여부를 질문하며
# 있으면 False, 없으면 True이다.
s = "python programming"
print("a" in s, "z" in s)
print("pro" in s, "x" not in s)