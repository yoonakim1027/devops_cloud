import pymysql

conn = None  # 접속할 때 쓸 애
cur = None  # 내가 조정할 수 있게 execute

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='1234',
                       db='sqlDB',
                       charset='utf8')  # 내 로컬 호스트에 접속
# 커서
cur = conn.cursor()

# userTBL의 회원 데이터 insert
# 넣을 컬럼들을 미리 알아둬야함
# userID, name, birthYear, addr -> 이거를 제약조건으로 둬야함

# <<<< 과제 >>>>
# 화면캡쳐 내이름
# userID, name, birthYear, addr, mobile1, mobile2, height
# insert / while 바꿔야함
# 새롭게 등록할 때 모든 데이터를 insert
# 기존데이터는 신경안써도 돼
# 숫자타입인지 아닌지 구분

# 실제 사용할 쿼리문
sql = ""

# 사용자에게 입력받을 데이터
userID = ""
name = ""
birthYear = ""
addr = ""

# 새로
mobile1 = ""
mobile2 = ""
height = ""
while (True):
    userID = input("사용자 ID ==> ")
    if userID == "":
        break  # 입력안되면 멈추기
    name = input("사용자 이름 ==> ")
    if name == "":
        break  # 입력안되면 멈추기
    birthYear = input("사용자 출생년도 ==> ")
    if birthYear == "":
        break  # 입력안되면 멈추기
    addr = input("사용자 주소 ==> ")
    if addr == "":
        break  # 입력안되면 멈추기

# 새로 추가
    mobile1 = input("사용자 핸드폰 번호(010)==> ")
    if mobile1 == "":
        break  # 입력안되면 멈추기
    mobile2 = input("사용자 핸드폰 번호 ==> ")
    if mobile2 == "":
        break  # 입력안되면 멈추기
    height = input("사용자 키 ==> ")
    if height == "":
        break  # 입력안되면 멈추기

    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mobile1, mobile2, height, mdate) VALUES " \
          "('" + userID + "' ,'" + name + "', "+ birthYear + ", '" + addr + "','" + mobile1 + "','"+ mobile2 +"', " + height +", CURDATE())"
    print(sql) # 모르겠으면 이걸로 확인해
    cur.execute(sql) #쿼리를 실행해라

conn.commit()
conn.close() # 엔터치면 종료됨 !


