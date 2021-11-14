import requests
from bs4 import BeautifulSoup


def check_available(received_text: str) -> bool:
    return received_text.startswith("네이버 검색:")  # 공백, 콜론포함 7개


def make_response(received_text: str) -> str:  # 처음 7자(공백, 콜론포함)뺀 것이 검색어
    query = received_text[7:]  # 공백,콜론 포함 7개
    post_list = naver_search(query)
    response_text = "\n".join(
        [post['title']
         for post in post_list])
    return response_text


def naver_search(query):
    naver_search_url = "https://search.naver.com/search.naver"
    params = {
        "where": "view",
        "sm": "tab_jum",
        "query": query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [
        {"title": tag.text}
        for tag in soup.select(".lst_total .total_tit")]
