import requests
from sentMail import sentMail

request = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-06-30&sortBy=publishedAt&apiKey=c2f58db2e47f4cd0a95f4c863c4ba298")
content = request.json()

body = ""
for article in content["articles"]:
    body = article["author"]

print(body)
sentmail(message=body)