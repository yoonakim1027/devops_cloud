

# test_ 로 시작되는 파일 / test_로 시작되는 함수 -> pytest가 수집
#모든 test_는 핵심적인 역할

# reverse_string
"""
거꾸로 글자 출력하기 
"""

def check_available(received_text:str)-> bool: #인자로 메시지를 받음    # -> 함수의 인자와 리턴값에 대한 타입을 명시
    return received_text.startswith("거꾸로:")
# 받은 메시지가 있어야 그걸 기반으로 응답을 만듬
def make_response(received_text:str) -> str:
    return received_text[4:][::-1].strip() # 좌우 공백 제거

### .strip() # 좌우 공백 제거


