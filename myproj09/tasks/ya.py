def check_available(received_text: str) -> bool:  # 인자로 메시지를 받음
    # -> 함수의 인자와 리턴값에 대한 타입을 명시
    return received_text == "야"


# 받은 메시지가 있어야 그걸 기반으로 응답을 만듬
def make_response(received_text: str) -> str:
    return "왜?"

# 새로운 메시지가 있을 때 마다 매번 고민하는 것이 아니라,
# 두개의 함수를 모든 task에서 일관되게 구분 -> 동일한 인터페이스를 가지기 때문에
# 관리하기 좋은 어플리케이션이 되는 것.
