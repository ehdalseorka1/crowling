import requests
from bs4 import BeautifulSoup

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

# bs_obj를 받아서 price를 return하게
def get_price(company_code):
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text

# bs_obj를 받아서 candle_chart_data를 return하게
def get_candle_chart_data(company_code):
    bs_obj = get_bs_obj(company_code)
    td_first = bs_obj.find("td", {"class":"first"})
    blind = td_first.find("span", {"class":"blind"})

    #close 종가(전일)
    close = blind.text

    return close

# samsung 005930
# naver 035420
# kakao 035720
company_codes = ["005930", "035420", "035720"]
for item in company_codes:
    price = get_price(item)
    close = get_candle_chart_data(item)
    print(price, close)




