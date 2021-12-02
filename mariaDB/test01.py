import pymysql

conn = None  # 접속할 때 쓸 애
cur = None  # 내가 조정할 수 있게 execute

# 데이터베이스 접속
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='1234',
                       db='sqldb',
                       charset='utf8')  # 내 로컬 호스트에 접속
# 커서
cur = conn.cursor()



# 실제 사용할 쿼리문
# << 파이썬에서 IFNULL 처리하기>>
# 쿼리문에 세미콜론 들어가면 오류난다! 안들어게 조심하기
sql = "SELECT breed, color, sex, age, size, find_date, protected_place FROM lostpettbl"
# 세미콜론 제외하고 복사

cur.execute(sql)

print("공고번호  색상  성별  나이  몸집크기  접수일시  보호장소")
print("--------------------------------------------------------------")

# breed, color, sex, age, size, find_date, protected_place
# 기본적으로 while으로 시작 -> break로만 빠져나가게 해주기만 하면 돼
while(True): #row 값이 없을 때 정지
    row = cur.fetchone()
    if row == None:# for문을 다 돌아서 돌게 없는 상황
        break
    breed = row[0]
    color = row[1]
    sex = row[2]
    age = row[3]
    size = row[4]
    find_date = row[5]
    protected_place = row[6]


    print("%5s %5s %5s %d %5s %5s %5s" % (breed, color, sex, age, size, find_date, protected_place))

conn.commit()
conn.close() # 엔터치면 종료됨 !


