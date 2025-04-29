import requests
from bs4 import BeautifulSoup
from io import BytesIO
import re



class SearchData():
    def __init__(self, query):
        response = requests.get(f"https://www.sinemalar.com/ajax/search/autocomplete/?query={query}")

        content = BeautifulSoup(response.content, "html.parser").find_all("a")

        self.results = []

        for e in content:
            tür = e['href'].split('/')[3]
            if tür != "film" and tür != "dizi":
                break
            print(tür)

            dict = {"Name": e.find('div', class_='card-title').text,
                    "Type": tür,
                    "Pic": BytesIO(requests.get(e.find("img").get("src")).content),
                    "URL": e.get("href")

                    }

            self.results.append(dict)


class FetchData():

    def __init__(self, URL):
        response = requests.get(URL)
        content = BeautifulSoup(response.content, "html.parser")

        info = content.find(class_=["column", "metadata"])


        self.result = {"name": content.find("h1").text.strip(),
            "year": info.find("a").text
        }



        for e in info.find_all("div"):
            try:
                if e.find("b").text == "Yönetmen:":
                    self.result["director"] = e.find("a").text
            except:
                pass

        picURL = content.find(class_= ["display-card", "poster"]).find("img").get("src")

        self.pic = BytesIO(requests.get(picURL).content)

        print(self.result)



        # _info = content.find_all(class_="info-group")
        # self.result = {}
        #
        # for e in _info:
        #     try:
        #         if e.find(class_="label-title").text == "Yönetmen:":
        #             self.result["director"] = e.find(class_="label").get_text(strip=True)
        #         elif e.find(class_="label-title").text == "Yapımı:":
        #             self.result["year"] = re.findall(r'\b(?:19|20)\d{2}\b', e.get_text("/", strip=True))[0]
        #     except:
        #         pass
        #
        #
        # self.result["name"] = content.find("h1").text
        #
        # _showPosterTpl = BeautifulSoup(content.find(id="showPosterTpl").text, "html.parser")
        # picURL = _showPosterTpl.find(class_="poster").get("src")
        #
        # self.pic = BytesIO(requests.get(picURL).content)


