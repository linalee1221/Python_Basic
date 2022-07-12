# 변수명은 대소문자가 다르면 철자가 같아도 다른 변수로 인식된다.
tomato = "토마토"
Tomato = "토메이러"
toMaTo = "틈메이러"
print(tomato)
print(Tomato)
print(toMaTo)
print(id(tomato))
print(id(Tomato))
print(id(toMaTo))