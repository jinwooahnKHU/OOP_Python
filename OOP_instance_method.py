# 객체가 가지고 있는 속성은 변수로 표현되고, 객체의 행동은 함수로 정의된다.
# 여기서 함수는 'method'라고 부른다.
# 따라서 class 안에서 함수를 정의하면 'method를 정의했다' 와 같다.

# 메소드의 3가지 종류
# 1. instance method
# 2. class method
# 3. static method


# instance method
# -> instance 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메소드
# 사용법 : 1) classname.methodname(instance) 2) instancename.methodname()
class User:
    def say_hello(some_user):  # sayhello는 instance method
        # .name을 통해 인스턴스 변수를 사용
        print('안녕하세요! 저는 {} 입니다.'.format(some_user.name))

    def login(some_user, my_email, my_password):
        if (some_user.email == my_email and some_user.password == my_password):
            print('로그인 성공')
        else:
            print('로그인 실패')


user1 = User()
user2 = User()

user1.name = '김대위'
user1.email = 'captain@khu.ac.kr'
user1.password = '12345'

user2.name = '강영훈'
user2.email = 'younghood@khu.ac.kr'
user2.password = '98766'


User.say_hello(user1)  # user1의 name을 사용
User.say_hello(user2)  # user2의 name을 사용

user1.say_hello()  # 이렇게도 사용할 수 있다. 인스턴스 변수가 첫번째 parameter로 들어간다.

user1.login(user1, 'captain@khu.ac.kr', '12345')
user1.login('captain@khu.ac.kr', '12345')
# 여러 parameter로 method 정의 시, user1이 첫 번째 Parameter로 들어간다.
