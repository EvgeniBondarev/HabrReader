import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #проверка сертификата


def pars_posts(user_habrs):
    for habr in user_habrs:
        if habr == "all":
            url = "https://habr.com/ru/all/",
        else:
            url = f"https://habr.com/ru/hub/{habr}/"

        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, "html.parser")
        posts = soup.find_all("article", class_="tm-articles-list__item")

        all_habrs = []

        for post in posts:
            post_id = post.get("id")
            link = post.find("a", class_="tm-article-snippet__title-link").get("href")
            rating = post.find("div", class_="tm-data-icons").find("div", class_="tm-votes-meter tm-data-icons__item").find("svg", class_="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article").find("title").text

            all_habrs.append({
                "post_id": post_id,
                "link": "https://habr.com" + link,
                "rating": rating
            })

        return all_habrs

