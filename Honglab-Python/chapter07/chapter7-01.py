# Class
# Instance

# 클래스의 구성
# 속성 (attribute)
# - 데이터 속성 (data attribute)
# - 메써드 (method)

class MyInt:
    # 메써드 정의 함수처럼 def 사용
    # self 는 메써드를 호출하는 객체

    # 클래스 변수 (class variable)
    # 모든 객체가 공유

    # 인스턴스 변수 (instance variable)
    # 각 객체마다 따로 가짐
    def __init__(self, value):
        # Dunder (Double Underscores)
        # 객체를 만들 때 자동으로 호출 constructor 와 비슷
        self.value = value # 인스턴스 변수

    def add(self, a):
        self.value = self.value + a


class MyClass:
    pass


i = MyClass()

print(type(i))

# namespace
# 변수, 함수, 클래스 등 여러가지 이름들이 들어있는 공간을 의미

print(dir())

print(__name__)

# __name__ 은 모듈 이름을 알려준다.
# 이때 모듈을 통하지 않고 직접 실행한 스크립트 에서는 __main__ 이란 특별한 값을 가진다.


class MyClass2:
    def __init__(self):
        self.my_variable = "hello world"

    def my_method(self):
        pass


i2 = MyClass2()

print(i2.my_variable) # hello world
i2.my_method()

print(dir(i2))


"""
📦 전역 네임스페이스
│
├── MyInt            ← 클래스 이름
├── MyClass
├── MyClass2
├── i                ← MyClass 인스턴스
├── i2               ← MyClass2 인스턴스
├── __name__         ← '__main__'
├── print, dir       ← 내장 함수
│
└── 클래스 내부 네임스페이스 (별도로 존재)
      └── __init__, add, my_variable ...
"""