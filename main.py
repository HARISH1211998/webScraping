import requests

request = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-06-30&sortBy=publishedAt&apiKey=c2f58db2e47f4cd0a95f4c863c4ba298")
content = request.json()
print(content)

for article in content["articles"]:
    print(article["author"])
    print(article["title"])
