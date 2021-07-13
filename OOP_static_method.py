class User:
    count = 0


    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1
    
    def say_hello(self):
        print('안녕하세요! 저는 {}입니다.'.format(self.name))

    def __str__(self):
        return '사용자: {}, 이메일: {}, 비밀번호 ***'.format(self.name, self.email)
    
    @classmethod
    def number_of_users(cls):
        print('총 유저 수는: {}입니다.'.format(cls.count))
    

    # @staticmethod를 붙혀주지 않으면, self인자가 파라미터에 처음에 들어가게 됨.
    # 따라서 인스턴스를 생성해주어야 사용이 가능함. 따라서 데코레이터를 붙혀주어야 함
    @staticmethod
    def is_valid_email(email_address):
        return '@' in email_address


print(User.is_valid_email('taehosung'))
print(User.is_valid_email('taehosung@khu.ac.kr'))
