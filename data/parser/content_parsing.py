def get_info(page):
    from bs4 import BeautifulSoup
    import fake_useragent
    import requests

    user = fake_useragent.UserAgent().random
    headers = {"User-Agent": user}

    response = requests.get(page, headers=headers).text
    soup = BeautifulSoup(response, "lxml")

    # photos
    block_photos = soup.find("div", id="image-box")
    photo_urls = list(map(lambda a: a.get("href"), block_photos.find_all("a")))

    # all description
    block_description = soup.find("div", id="tab-description")

    # short description
    short_description = block_description.find("span", class_="prod_descr__h2_color").text

    # description
    description = block_description.find("p").text
    description = description.replace("Характеристики:", "").replace("Поради щодо використання:", "").strip()

    # price
    price = soup.find("span", class_="price-rrc__price").text

    # specifications
    block_specifications = soup.find("div", id="tab-specification")
    all_specifications = block_specifications.find_all("div", class_="short-attribute")

    specifications = dict()

    for spec in all_specifications:
        name = spec.find("span", class_="attr-name").text
        text = spec.find("span", class_="attr-text").text

        specifications[name.replace("  ", " ")] = text.replace("  ", " ")

    return photo_urls, short_description, description, specifications, price
