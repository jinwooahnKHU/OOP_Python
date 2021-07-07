# __str__ method (dunder method)
# -> print 함수로 호출할 때 자동으로 작동 됨

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호 : *****".format(self.name, self.email)


user1 = User('김대위', 'captain@khu.ac.kr', '12345')

print(user1)
