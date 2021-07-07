# Class 변수 : 같은 class의 instance끼리 공유하는 변수

# 앞서 작성했던 instance 변수는 '자신만의 변수'라면, class 변수는 class 내의 객체끼리 공유하는 변수

class User:
    count = 0  # class 변수 선언은 class명 바로 밑에서 해주면 된다

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1  # __init__을 이용해서 객체를 생성할 때마다 count 가 1씩 증가


user1 = User('김영훈', 'younghoon@khu.ac.kr', '12345')
user2 = User('이윤수', 'yoonsoo@khu.ac.kr', '34244')
user3 = User('서혜린', 'hyelin@khu.ac.kr', '31212')

print(User.count)  # class 변수 출력법
