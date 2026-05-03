import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = []

rows = soup.select(".athing")

for row in rows:
    
    title_tag = row.select_one(".titleline a")
    title = title_tag.text if title_tag else None
    link = title_tag["href"] if title_tag else None

    # subtext is in next row
    subtext = row.find_next_sibling("tr").select_one(".subtext")

    points = subtext.select_one(".score")
    points = points.text if points else "0 points"

    time_tag = subtext.select_one(".age")
    time = time_tag.text if time_tag else None

    articles.append({
        "title": title,
        "url": link,
        "points": points,
        "published_time": time
    })

df = pd.DataFrame(articles)

print("Rows:", len(df))
print(df.head())

df.to_csv("hackernews_raw.csv", index=False)
df.to_csv("hackernews_raw.csv", index=False)