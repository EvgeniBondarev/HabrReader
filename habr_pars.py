import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #проверка сертификата

HUBS = {
    "all":"https://habr.com/ru/all/",
    "programming":"https://habr.com/ru/hub/programming/",
    "python":"https://habr.com/ru/hub/python/",
    "read":"https://habr.com/ru/hub/read/"
}

def pars_posts(hubs_type):
    url = HUBS[hubs_type]
    page = requests.get(url, verify=False)

    soup = BeautifulSoup(page.content, "html.parser")

    posts = soup.find_all("article", class_="tm-articles-list__item")

    for post in posts:
        post_id = post.get("id")
        link = post.find("a", class_="tm-article-snippet__title-link").get("href")
        rating = post.find("div", class_="tm-data-icons").find("div", class_="tm-votes-meter tm-data-icons__item").find("svg", class_="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article").find("title").text

        print("Post-ID:", post_id)
        print("Link:", "https://habr.com" + link)
        print("Rating:", rating)
        print("="*50)
