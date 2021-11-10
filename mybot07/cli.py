# while True:  # 항상 참 -> 무한루프
#     break  # 이때 끝남


# while True:  # 항상 참
#     line = input("Enter question : (quit : q) ")  # 한줄 입력받기
#     if line == "q":  # 만약 입력받은 값이 q라면 break
#         print("안녕, 잘 가.")
#         break  # q하면 빠져나가기
# # "네이버 검색 : 파이썬" -> 파이썬만 가져와서 검색어로 쓰겠다.
#     elif line.startswith("네이버 검색 : "):# in은 포함이라서 그것보다는
#     # startswith -> 문자열이 네이버로 시작한다면?
#         query = line [7:] # 검색어로 쓰겠다.
#         title_list  = naver_search(query)
#         print("=== 네이버 검색 결과 : {query}===")
#         print(title_list)

#     elif line == "야":
#         print("왜?")

#     else:
#         print("니가 무슨 말을 하는 지 모르겠어.")


###  명령 프롬포트에 설치 : pip install requests beautifulsoup4
#### 네이버 검색창 명령 프롬포트에서 실행해보기 ####
import requests
from bs4 import BeautifulSoup

# 항상 타입을 잘 봐야함


def naver_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [tag.text for tag in soup.select(".lst_total .total_tit")]


while True:
    line = input("Enter question (quit: q): ")
    if line == "q":
        print("안녕. 잘 가.")
        break
    # "네이버 검색 : 파이썬" # 아예 이렇게 써야함
    # "네이버 검색 : 여기에 검색하고 싶은 것 "
    elif line.startswith("네이버 검색 :"):
        query = line[7:]  # 검색어
        title_list = naver_search(query)
        print(f"=== 네이버 검색 결과 : {query} ===")
        for idx, title in enumerate(title_list, 1):
            print(f"[{idx}] {title}")
    elif line == "야":
        print("왜?")
    else:
        print("니가 무슨 말을 하는 지 모르겠어.")
