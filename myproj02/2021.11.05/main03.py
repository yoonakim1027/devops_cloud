# 랜덤 숫자 맞추기
from random import randint

number = randint(1, 100)
for retry in range(10):
    line = input(f"[ {retry} ] Try guess number : ")  # 몇 번째 시도인지 앞에 적힐것.
    # 입력받을 문자열
    # answer = int(line or 0) # 빈 문자열은 정수로 변환할때 오류가 생김!
    # or은 앞에것이 거짓일 경우 뒤의 값인 0을쓴다는 뜻
    answer = int(line.strip() or 0)  # .strip() 좌우 정렬해줌 ex) 스페이스 제거 등

    if answer == number:
        # pass # 코드 구현전에 pass를 사용해서 자리를 만듬
        print(f"{retry}회 시도에 성공")
        break  # 맞추고 나오면 break !

    elif answer < number:  # if만 써도돼~
        print(" 더 큰 수를 입력해주세요. ")
    else:
        print(" 더 작은 수를 입력해주세요. ")
else:  # 의도한 횟수를 다 채웠을때, 더 이상 가져올 for없이 정상 수행 후 끝난다면 출력
    # 굳이 10회되면 끝내라~ 할필요도 없이! break를 만나면 실행은 안됨 !
    print("다음 기회에...")


# 너무 모든것을 생각해서 만드는 것은 복잡해지는 길임~
# 시작은 최소한 간소하게 만들면 됨~

# MVP Minimum Valuable Product
# 초기에 프로그램을 만들때 이렇게 프로그램을 만듬.
# 내가 이 프로그램을 만들기 전에 검증!
# 처음부터 모든걸 한번에 올리기엔 어려우니까
# 처음에 먼저 간소하게 구성한 뒤 살붙이기~

"""
랜덤 숫자를 맞춰보세요.
hint: random.randint를 통해 1이상 100이하의 랜덤수를 만듭니다.
유저에게 10회의 기회를 줍니다.
 - 그 숫자를 정확히 맞췄다면, 몇 번 만에 맞췄는 지 출력
 - 입력한 숫자가 랜덤수보다 작다면, "더 큰 수를 입력해주세요." 라고 출력
 - 입력한 숫자가 랜덤수보다 크다면, "더 작은 수를 입력해주세요."라고 출력
 - 횟수를 초과했다면, "다음 기회에 ..." 라고 출력
"""

from random import randint

number = randint(1, 100)

for retry in range(1, 11):
    line = input(f"[{retry}] Try guess number : ")
    try:
        answer = int(line.strip())

        # answer = int(line.strip() or 0)
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
        continue

    if answer == number:
        print(f"{retry}회 시도에 성공.")
        break
    elif answer < number:
        print("더 큰 수를 입력해주세요.")
    else:
        print("더 작은 수를 입력해주세요.")
else:
    print("다음 기회에 ...")
