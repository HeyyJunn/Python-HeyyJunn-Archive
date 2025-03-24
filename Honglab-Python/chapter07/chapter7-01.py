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
