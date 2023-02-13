import requests
from bs4 import BeautifulSoup
import urllib3
import re
from dataclasses import dataclass

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #проверка сертификата

@dataclass
class HabrsData:
    """rating: str, link: str, reading_time: str"""
    rating: str
    link: str
    reading_time: str
    type: str
    def is_positive(self, percent, vote):
        nums_in_rating = re.findall(r'\d+', self.rating)
        nums_in_rating = [int(i) for i in nums_in_rating]
        positive_percentage = 100 * nums_in_rating[1] / nums_in_rating[0]

        if positive_percentage > percent and nums_in_rating[0] > vote:
            return True
        else:
            return False


def pars_posts(user_habrs: list[str], user_rercent: int, user_vote: int) -> list[HabrsData]:
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
            rating = post.find("div", class_="tm-data-icons").find("div", class_="tm-votes-meter tm-data-icons__item").\
                          find("svg", class_="tm-svg-img tm-votes-meter__icon tm-votes-meter__icon tm-votes-meter__icon_appearance-article").\
                          find("title").text
            link = post.find("a", class_="tm-article-snippet__title-link").get("href")
            reading_time = post.find('span', class_="tm-article-reading-time__label").text

            post_data = HabrsData(rating, "https://habr.com" + link, "Время прочтения:" + reading_time.replace("\n", ""), habr)

            if post_data.is_positive(user_rercent, user_vote):
                all_habrs.append(post_data)

    return all_habrs

