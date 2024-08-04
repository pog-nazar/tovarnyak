from bs4 import BeautifulSoup
import pickle


urls = list()

for page in range(1, 23+1):

    with open(f"../pages/page{page}.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "lxml")

    content_block = soup.find("div", id="content").find("div", class_="row-flex category-page")
    content = content_block.find_all("div", class_="product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-6 col-lg-1-5")

    cont = 0

    for c in content:
        cont += 1

        div_url = c.find("div", class_="image")
        content_url = div_url.find("a").get("href")

        urls.append(content_url)

    print(page)

with open("../products/serialized_urls", "wb") as file:
    pickle.dump(urls, file)
