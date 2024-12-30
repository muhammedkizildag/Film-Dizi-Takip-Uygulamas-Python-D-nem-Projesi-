import requests
from bs4 import BeautifulSoup
from io import BytesIO
import re



class SearchData():
    def __init__(self, query):
        response = requests.get(f"https://www.sinemalar.com/ajax/search/autocomplete/?query={query}")

        content = BeautifulSoup(response.content, "html.parser").find_all("li")

        self.results = []

        for e in content:
            tür = e.find_all("span")[-1].text if e.find_all("span") else None
            if tür != "Film" and tür != "Dizi":
                break

            dict = {"Name": e.find("a").get_text(strip=True, separator="/").split("/")[0],
                    "Type": e.find_all("span")[len(e.find_all("span"))-1].text,
                    "Pic": BytesIO(requests.get(e.find("img").get("src")).content),
                    "URL": e.find("a").get("href")
                    }
            self.results.append(dict)


class FetchData():

    def __init__(self, URL):
        response = requests.get(URL)
        content = BeautifulSoup(response.content, "html.parser")

        _info = content.find_all(class_="info-group")
        self.result = {}

        for e in _info:
            try:
                if e.find(class_="label-title").text == "Yönetmen:":
                    self.result["director"] = e.find(class_="label").get_text(strip=True)
                elif e.find(class_="label-title").text == "Yapımı:":
                    self.result["year"] = re.findall(r'\b(?:19|20)\d{2}\b', e.get_text("/", strip=True))[0]
            except:
                pass


        self.result["name"] = content.find("h1").text

        _showPosterTpl = BeautifulSoup(content.find(id="showPosterTpl").text, "html.parser")
        picURL = _showPosterTpl.find(class_="poster").get("src")

        self.pic = BytesIO(requests.get(picURL).content)


