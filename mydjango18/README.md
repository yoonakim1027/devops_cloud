(1)html 상에서, url 을 기입하는 속성 3가지

주소 : http://example.com/blog/1002/comments
-> 위의 주소가 저 밑에 기입되는 것임 
- <img src=""/>
- <script src=""></script>
- <link href=""/>
- <a href=""></a>
- <form action=""></form>



- <img src="flower.jpg"/> -> http://example.com/blog/1002/comments/flower.jpg
- <img src="../flower.jpg"/> -> http://example.com/blog/flower.jpg (위에것에서 한단계 상승)
- <img src="/flower.jpg"/> -> http://example.com/flower.jpg


# 이미지가 있으면 불러오고, 없으면 아니고~ 

- <script src=""></script>
- <link href=""/>
- <a href=""></a>
- <form action=""></form>


(2)
(2-1) HTML Form (클라이언트 측)
- 클라이언트에서 사용자에게 입력폼을 제공, 이를 서버로 전송하려 할때 
- 서식에서 입력된 값을 서버로 보내면? -> 유효성검사
- 이제 서버에서는 입력값에 오류가 없는 지 검사
- 코로나라고 하면, 주민번호는 잘 맞는지~ 휴대폰번호가 잘맞는지 등등 다양한 검사가 있음
- 이렇게 입력을 다 검색해야함.
- 절대로 유저가 입력한 값이 당연히 다 잘 입력되었겠지 생각하면 안됨 
- 유효성 검사 및, 검사 통과 시에 저장하는것 / 검사 실패 시 에러 화면 띄우기
- 유효성 검사 후 성공 / 실패 이렇게 처리되는 로직이 달라질 수 있음


(2-2) django Form (서버 측)
- 유저들의 입력값에 대한 유효성 검사가 훨씬 수월함
- djagno form을 사용하지 않으면 django사용이 의미가 없을 정도 ~ 
