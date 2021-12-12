# 2021.12.06
# 포스팅 : 제목, 내용, 글쓴이

post = ('제목', '내용', '글쓴이')
# 각각의 값들에 접근하기 위해서, 인덱스로 접근해야 함
post[0]
post[1]
post[2]

# namedtuple

from collections import namedtuple

namedtuple('Post', 'title content author_name')

post = Post('제목', '내용', '글쓴이')
post.title, post.content, post.author_name


# 어떤 데이터 - 어떤 데이터와 연결된 로직이 필요 -> 이게 함수

# 관련된 데이터, 관련된 함수를 묶는 것 -> 클래스
# 붕어빵과 붕어빵 틀  ?

# 어떤 데이터 - 그 데이터를 처리하는 함수들을 하나로 묶는 것이 클래스 !

# 클래스의 이름은? 첫글자는 무조건 대문자로 씀 -> CapitalCase
# 코드에도 코드 스타일, 문체가 존재한다 ! 코드 스타일에 대한 고민이 필요함 .

class Post:  # 데이터 + 함수 같이 처리
    def __init__(self, title, content, author_name):  # 생성자(Constructor)
        # title = "" -> 지역변수. 함수가 호출될때만 사용되고 끝나면 사라짐
        self.title = title  # 이렇게 해줘야함.
        self.content = content
        self.author_name = author_name
        # __init__ : 명시적으로 호출하는 것은 아님!
        # 함수에서 호출한 값을 얘네가 받는 것 !

    def check_content(self):  # self가 붙으면 인스턴스 함수
        if len(self.content) == 0:
            pass


# 클래스에 대한 속성을 정의할 때에는?
# 클래스 안에 데이터 +관련 함수를 묶는데, 여기서 가장 먼저 해야할 함수정의는?
# def __init__(self):

# 클래스는 클래스일뿐, 함수가 아님.
# 어떤 데이터와 관련된 함수들을 묶어놓은 것. 클래스 자체가 함수는 아님
# 그래서 클래스 이름을 쓰고 호출을 하면?
# 이 인자들을 위의 def __init__ 가 받게되는 것
# 3개 넘기도록 했으면 위에서도 3개를 받아야 하는 것.!
# 근데 왜  def __init__(self,title, content, author_name): -> 이렇게 네개일까?
# 가장 처음에 쓰는 self는 없는애라고 생각하면 돼!
# 값을 붙잡아 두기 위해,  self.content = content 이런식으로 붙잡아 두는 것!

post.title  # 얘가 의미 하는것은 ? self.title -> self에 묶인 title
post.author_name  #
post.content  # 클래스 활용은 namedtuple 쓰는 방법과 비슷!

post = Post('제목', '내용', '글쓴이')

post.check_content()  # 클래스 안에 있는 함수를 사용하기 위해서는 ?
# 클래스 안에 있기 때문에, .함수명() 이렇게 접근하면 돼


# 클래스 타입의 새로운 변수를 인스턴스라고 함
post1 = Post()

# 인스턴스 던전 - > 새로운 파티가 들어갈때마다, 새로운 던전이 생성


# 인스턴스 함수 - ? 인스턴스를 통해서만 호출할 수 있는 함수
# 클래스 함수 - ? 클래스를 통해서만 호출할 수 있는 함수


# class Post:
# def 함수명(self): #이게 인스턴스 함수
# self는 약속같은 존재 !


# 클래스명.클래스함수명() # 이게 클래스 함수

# __ 이렇게 언더바 두개를 쓰는 것은 ? 파이썬에서 자체적으로 역할을 부여한 경우!
# 우리가 역할을 주고 싶다면? __언더바 두개를 써서 만들면 안돼


# 인스턴스, 객체, 개체 - > 클래스 타입의 새로운 변수를 만들어내는 것!
# 인스턴스 던전 처럼

# 새로만들 변수명 = 클래스이름  -> 쓰고, (함수호출 처럼)

# 클래스에는 return을 안해도 돼 !
