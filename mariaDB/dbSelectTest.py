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



# 실제 사용할 쿼리문
# << 파이썬에서 IFNULL 처리하기>>
# 쿼리문에 세미콜론 들어가면 오류난다! 안들어게 조심하기
sql = "SELECT userID, name, birthYear, addr, CONCAT(mobile1,'-',mobile2) AS mobile, height, mdate FROM userTBL"
# 세미콜론 제외하고 복사

cur.execute(sql)

print("회원ID  회원명 출생년도  주소     연락처      키    가입일")
print("--------------------------------------------------------------")

# 기본적으로 while으로 시작 -> break로만 빠져나가게 해주기만 하면 돼
while(True): #row 값이 없을 때 정지
    row = cur.fetchone()
    if row == None:# for문을 다 돌아서 돌게 없는 상황
        break
    userID = row[0]
    name = row[1]
    birthYear = row[2]
    addr = row[3]

    # None Type 처리 추가
   if row[4] == None:
        mobile = '-'
    else:
        mobile = row[4]
    if row[5] == None:
        height = 0
    else:
        height = row[5]

    if row[6] == None:
        mdate = '-'
    else:
        mdate = row[6]

    print("%5s %5s %d %5s %10s %d %5s" % (userID, name, birthYear, addr, mobile, height, mdate))

conn.commit()
conn.close() # 엔터치면 종료됨 !


