print(type(123))
print(type("Hello, World!"))

name = input("What is your name? ")
print(f"Hello, {name}")


# 함수 정의(def) 앞에는 빈 줄 두 줄을 띄우는 게 Python의 스타일 권장사항입니다.
def input_and_output():
    name1 = input("What is your name? ")
    print(f"Hello, {name1}")


input_and_output()
input_and_output()
