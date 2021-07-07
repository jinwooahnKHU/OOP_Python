# self : python에서는 instance method의 첫 번째 parameter의 이름을 'self'로 쓰라고 권장한다.
# initialize 함수를 설정하면 인스턴스 변수 할당 시 편하다
# Magic Method(aka special method) : 특정 상황에서 자동으로 호출되는 메소드
class User:
    # __init__은 instance가 생성될 때 자동으로 호출
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("저는 {} 입니다.".format(self.name))

    def login(self, my_email, my_password):
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공")
        else:
            print("실패")

    def check_name(self, name):
        return self.name == name


user1 = User("김대위", 'captain@khu.ac.kr', '12345')

user1.say_hello()

print(user1.check_name('김대위'))
