from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('a','link_favorsch')

rank=1

search_rank_file = open("rankresult.txt","a")

today = DateFormat(datetime.now()).format('Y년m월d일')

print(datetime.today().strftime(today+"의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1