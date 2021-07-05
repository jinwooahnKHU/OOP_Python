# class 이름 첫글자는 항상 대문자!
class User:
    # 내용(속성과 행동)
    pass


user1 = User()  # User인스턴스(객체)가 생기고 user1이 instance를 가리키게 됨
user2 = User()
user3 = User()

# 위의 세 인스턴스는 다 다른 인스턴스다

# 속성 추가하기(변수와 비슷하다)
# 인스턴스 변수 정의하기 : 인스턴스이름.속성이름(인스턴스변수)='속성에 넣을 값'
# 인스턴스 변수 : instance가 개인적으로 가지고 있는 속성
user1.name = "김대위"
user1.email = 'captain@khu.ac.kr'

# 인스턴스 변수 사용하기
# 인스턴스이름.인스턴스변수이름

print(user1.email)
