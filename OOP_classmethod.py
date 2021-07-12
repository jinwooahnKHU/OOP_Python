class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

 
    @classmethod
    def from_string(cls, string_params):
        # cls은 User() 와 같이 instance를 생성하는 일을 한다.( cls은 class 그 자체이기 때문!!!)
        return cls(string_params.split(',')[0], string_params.split(',')[1],string_params.split(',')[2] )
        
        
    @classmethod
    def from_list(cls, list_params):
        
        return cls(list_params[0], list_params[1], list_params[2])

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

