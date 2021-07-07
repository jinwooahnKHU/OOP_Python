# Class Method : Class 변수의 값을 읽거나 설정하는 method

# 규칙 : 첫 번째 parameter로 class가 자동 전달된다!!(이를 일반적으로 cls라고 함)
# 따라서 class 변수를 가져올 때, cls를 쓰면 됨
# ex) cls.count 와 User.count은 같음

class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print('안녕하세요 저는 {} 입니다.'.format(self.name))

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ****".format(self.name, self.email)

    # class method은 정의 전에 무조건 아래처럼 먼저 적어주어야 한다
    # class method은 instance method 와 비슷하게 첫 parameter을 class로 받기에 cls라고(마치 self처럼) 해준다.
    @classmethod
    def number_of_users(cls):
        # 여기서 cls.count로 class 변수를 가져온다
        print('총 유저 수는 :{} 입니다.'.format(cls.count))


user1 = User('김영훈', 'younghoon@khu.ac.kr', '12345')
user2 = User('이윤수', 'yoonsoo@khu.ac.kr', '34244')
user3 = User('서혜린', 'hyelin@khu.ac.kr', '31212')


User.number_of_users()
user1.number_of_users()
