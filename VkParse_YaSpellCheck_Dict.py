import enchant
import requests
import time
import datetime
import xml.etree.ElementTree as ET
import re

d = enchant.Dict("ru_RU") # Словарь правильных слов и слов исключений
time_now = datetime.datetime.now()

token = "==Enter Here=="
version = "5.131"
domain = "==Enter Here==" # 


def vk_parse():
    post_get = 1
    # post_get_all = 20 # "введите ограничение на количество постов: ") or
    offset = 0 # "смещение относительно первого поста: ") or
    last_post_date = 0
    while True: # программа работает пока не наберёт post_count постов
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={
                                    "access_token": token,
                                    "v": version,
                                    "domain": domain,
                                    "count": post_get,
                                    "offset": offset
                                }
                                )
        data = response.json()["response"]["items"]
#        offset += post_get
        if "is_pinned" in data[0]:
            offset = 1
            continue
        post_id, post_from_id, post_date, post_text = data[0]["id"], data[0]["from_id"], data[0]["date"], data[0]["text"]
        if last_post_date < post_date:
            last_post_date = post_date
            post = re.findall(r"(?i)[А-Яа-яЁёСсЙй]+", post_text)
            post_time = datetime.datetime.fromtimestamp(post_date)
            post_link = f"https://vk.com/==Enter Here==?w=wall{post_from_id}_{post_id}"
            for j in post:
                if not d.check(j):
                    response = requests.get("https://speller.yandex.net/services/spellservice/checkText",
                                            params={
                                                "text": j
                                            }
                                            )
                    data = response.text
                    if "error" in data:
                        data = ET.fromstring(response.content)
                        sin = data[0][1].text
                        print(f"возможно ошибка -> {j} | {sin} | дата: {post_time} | ссылка: {post_link}")
            print(f"Пост {post_link} просканирован | время сканирования {time_now}")
        else:
            print("Ничего не нашёл:)")
        time.sleep(180)
        print("Проверяю...  ", end="")
vk_parse()
