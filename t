[1mdiff --git a/mariaDB/dbConnTest.py b/mariaDB/dbConnTest.py[m
[1mindex 2262a9b..7ddfecc 100644[m
[1m--- a/mariaDB/dbConnTest.py[m
[1m+++ b/mariaDB/dbConnTest.py[m
[36m@@ -30,10 +30,10 @@[m [msql = ""[m
 # 사용자에게 입력받을 데이터[m
 userID = ""[m
 name = ""[m
[31m-birthYear = ""[m
[32m+[m[32mbirthYear = "" # 초기화 하면서 타입이 정해지는것[m
 addr = ""[m
 [m
[31m-# 새로[m
[32m+[m[32m# 새로 변수선언[m
 mobile1 = ""[m
 mobile2 = ""[m
 height = ""[m
[36m@@ -62,6 +62,8 @@[m [mwhile (True):[m
     if height == "":[m
         break  # 입력안되면 멈추기[m
 [m
[32m+[m[32m# 쿼리할 때 작은 따옴표를 붙히지 않으면 정수형태임[m
[32m+[m[32m    # 모든 데이터를 입력하려면? 컬럼명은 명시하지 않아도 상관없었음![m
     sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mobile1, mobile2, height, mdate) VALUES " \[m
           "('" + userID + "' ,'" + name + "', "+ birthYear + ", '" + addr + "','" + mobile1 + "','"+ mobile2 +"', " + height +", CURDATE())"[m
     print(sql) # 모르겠으면 이걸로 확인해[m
[1mdiff --git a/mariaDB/dbGUItest.py b/mariaDB/dbGUItest.py[m
[1mindex 35b9e78..32d3704 100644[m
[1m--- a/mariaDB/dbGUItest.py[m
[1m+++ b/mariaDB/dbGUItest.py[m
[36m@@ -1,47 +1,207 @@[m
 import pymysql[m
[32m+[m[32mfrom tkinter import *[m
[32m+[m[32mfrom tkinter import messagebox[m
 [m
[31m-conn = None  # 접속할 때 쓸 애[m
[31m-cur = None  # 내가 조정할 수 있게 execute[m
 [m
[32m+[m
[32m+[m[32m# 커서 받은 다음에 select 기능 구현[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[32m# 제일 먼저 해야하는 것[m
[32m+[m[32m# import tkinter[m
[32m+[m
[32m+[m[32m# 데이터베이스 연동 함수[m
[32m+[m[32mdef insertData():[m
[32m+[m[32m    conn = None  # 접속할 때 쓸 애[m
[32m+[m[32m    cur = None  # 내가 조정할 수 있게 execute[m
 # 데이터베이스 접속[m
[31m-conn = pymysql.connect(host='127.0.0.1',[m
[31m-                       user='root',[m
[31m-                       password='1234',[m
[31m-                       db='sqlDB',[m
[31m-                       charset='utf8')  # 내 로컬 호스트에 접속[m
[31m-# 커서[m
[31m-cur = conn.cursor()[m
[32m+[m[32m    conn = pymysql.connect(host='127.0.0.1',[m
[32m+[m[32m                           user='root',[m
[32m+[m[32m                           password='1234',[m
[32m+[m[32m                           db='sqlDB',[m
[32m+[m[32m                           charset='utf8')  # 내 로컬 호스트에 접속[m
[32m+[m[32m    # 커서[m
[32m+[m[32m    cur = conn.cursor()[m
[32m+[m
[32m+[m[32m    # 회원 정보 insert 기능 구현[m
[32m+[m[32m    # 사용자에게 데이터를 받아야 함 (단독의 데이터 한 건씩이니까 리스트로 안해도 됨)[m
[32m+[m[32m    # 사용자에게 입력 받은 회원 정보 초기화[m
[32m+[m[32m    userID, name, birthYear, addr = "", "", "", ""[m
[32m+[m
[32m+[m[32m    # GUI에서 입력한 데이터 담기[m
[32m+[m[32m    userID = edit1.get()[m
[32m+[m[32m    name = edit2.get()[m
[32m+[m[32m    birthYear = edit3.get()[m
[32m+[m[32m    addr = edit4.get()[m
[32m+[m[32m# SELECT userID, name, birthYear, mdate[m
[32m+[m[32m    # 기본적으로 sql초기화[m
[32m+[m[32m    sql = ""[m
[32m+[m[32m    # sql 쿼리 만들기[m
[32m+[m[32m    sql = "INSERT INTO userTBL (userID, name, birthYear, addr, mdate) VALUES " \[m
[32m+[m[32m          "('" + userID + "' ,'" + name + "', " + birthYear + ", '" + addr + "', CURDATE())"[m
[32m+[m
[32m+[m[32m    # print(sql) #배포할 땐 지워야함 !!! 그냥 확인용으로만 ~ 공유할 때는 지우고 올려야함[m
[32m+[m[32m    # 쿼리 실행[m
[32m+[m[32m    # << 예외처리 >>[m
[32m+[m[32m    # 쿼리를 실행하면서, exception이 발생할 가능성이 높아짐 -> 사용자가 입력을 안할 경우, null값이 생길 경�