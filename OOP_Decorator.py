# Decorator function -> 다른 함수를 꾸며주는 함수
# 기존의 함수에 새로운 기능을 추가해준다

def print_hello():
    print('안녕하세요')

# add_print_to()가 decorator 함수!!


def add_print_to(original):  # original()이라는 함수를 매개변수로 받는다
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper  # 함수만을 return


# 아래는 실행시켜도 아무것도 결과가 나오지 않는다. -> add_print_tp(print_hello) 자체가 wrapper이기 때문!
# wrapper 함수 그 자체만을 return. 함수를 실행하는 것이 아니다
print(add_print_to(print_hello))

# 실행시키려면 아래와 같이 해야 함
print(add_print_to(print_hello)())


# Decorator함수를 간단하게 짜기

@add_print_to  # 밑의 함수에 add_print_to를 적용해라는 말. 즉, 꾸민 결과로 바로 만들어주는 작업!
def hello_world():
    print('안녕하세요')


print(hello_world())
