# 구구단 

# Breakpoint -> 프로그램을 실행하다가 이 지점에서 멈춰달라
for 숫자 in range(2, 10):
    print("### {}단 ###".format(숫자))
    for i in range(1, 10):
        계산결과 = 숫자 * i
        print("{} * {} = {}".format(숫자, i, 계산결과))
    print("")


