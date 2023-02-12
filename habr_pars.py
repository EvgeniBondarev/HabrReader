import requests
from bs4 import BeautifulSoup
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #проверка сертификата


def pars_posts(user_habrs):
    print(user_habrs)
    all_habrs = []
    for habr in user_habrs:
        if habr == "all":
            url = "https://habr.com/ru/all/",
        else:
            url = f"https://habr.com/ru/hub/{habr}/"

        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.content, "html.parser")
        posts = soup.find_all("article", class_="tm-articles-list__item")


        for post in posts:
            rating = post.find("div", class_="tm-data-icons").find("div", class_="tm-votes-meter tm-data-icons__item").find("svg", class_="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article").find("title").text

            nums = re.findall(r'\d+', rating)
            nums = [int(i) for i in nums]
            positive_percentage = 100 * nums[1] / nums[0]

            if positive_percentage > 75 and nums[0] > 50:

                link = post.find("a", class_="tm-article-snippet__title-link").get("href")
                reading_time = post.find('span', class_="tm-article-reading-time__label").text

                all_habrs.append({
                    "link": "https://habr.com" + link,
                    "rating": rating,
                    "reading_time": "Время прочтения:" + reading_time.replace("\n", ""),
                    "type": habr
                })
                print(positive_percentage)

    return all_habrs

