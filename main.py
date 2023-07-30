import requests
from sendmail import sendmail

request = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-06-30&sortBy=publishedAt&apiKey=c2f58db2e47f4cd0a95f4c863c4ba298")
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"


body = body.encode("utf-8")
sendmail(message=body)