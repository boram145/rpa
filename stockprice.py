import pywinmacro as pw
import time

location1=(204, 62) # 크롬 URL 창
location2=(327, 11) # 네이버 검색창
location3=(90, 512) # 종목명 버튼
location4=(251, 286) # 1년 주가그래프 버튼

def price():
    pw.click(location1)
    time.sleep(1)
    #크롬 검색 창 클릭
    pw.type_in("www.naver.com")
    time.sleep(1)
    # 네이버 URL 입력
    pw.key_press_once("enter")
    time.sleep(3)
    #엔터 쳐서 검색
    pw.click(location2)
    time.sleep(1)
    #초록창 클릭
    pw.type_in("네이버")
    time.sleep(1)
    #종목 입력
    pw.key_press_once("enter")
    time.sleep(3)
    #엔터 쳐서 검색
    pw.click(location3)
    time.sleep(3)
    #종목명 클릭
    pw.click(location4)
    #1년주가 그래프 클릭
