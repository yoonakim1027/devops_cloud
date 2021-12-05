-- CREATE DATABASE myproj11_db charset utf8mb4;
USE myproj11_db;
CREATE TABLE log(
   id int primary key auto_increment,
   message varchar(255) NOT NULL,
   broswer varchar(100) NOT NULL
   AUTO_INCREMENT=1
);


INSERT INTO log VALUES(NULL, '첫 로그', 'chrome');
INSERT INTO log VALUES(NULL, '두번째 로그', 'chrome');
INSERT INTO log VALUES(NULL, '세번째 로그', 'chrome');
INSERT INTO log VALUES(NULL, '네번째 로그', 'chrome');
SELECT * from log;

SELECT * FROM LOG WHERE id = 1 or 1;