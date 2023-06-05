import requests
from bs4 import BeautifulSoup
import csv

url = "https://cedec.cesa.or.jp/2023/session"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# セッション一覧を取得する
sessions = soup.find_all("div", class_="filtr-item")
print(len(sessions))

# CSVファイルを作成する
with open('sessions.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  # セッション一覧をCSVファイルに書き込む
  for session in sessions:
    categoryElements = session.find_all("div", class_="cate-type")
    categories = "/".join(map(lambda categoryElement: categoryElement.text, categoryElements))
    title = session.find("b", class_="session-title").text
    url = session.find("b", class_="session-title").parent.get("href")
    speaker = session.find("span", class_="medium-text").text.lstrip().rstrip()
    print("-----")
    print(categories)
    print(title)
    print(speaker)
    print(url)
    writer.writerow([
      categories,
      title,
      speaker,
      url
    ])
