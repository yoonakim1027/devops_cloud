import re

def check_available(received_text:str)-> bool: #인자로 메시지를 받음    # -> 함수의 인자와 리턴값에 대한 타입을 명시
    return received_text.startswith("숫자더하기:") # 6글자
# 받은 메시지가 있어야 그걸 기반으로 응답을 만듬
def make_response(received_text:str) -> str:
    line = received_text[6:]
    #1 개 이상의 숫자 문자열로 구성된 문자열 생성
    calculated_number = (sum(map(int,re.findall(r"\d+", line))))
    return calculated_number

#return received_text[6:][::-1].strip() # 좌우 공백 제거
# 6글자를 뺀 나머지
# test는 구현하기 전에 작성해두는 것이 좋음


# 정규 표현식
import re

sum(map(int,re.findall(r"\d+",s)))

