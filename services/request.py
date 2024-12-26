import requests
from bs4 import BeautifulSoup
from io import BytesIO



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
        print("run")
        response = requests.get(URL)
        content = BeautifulSoup(response.content, "html.parser")

        _info = content.find_all(class_="info-group")
        self.result = {}

        for e in _info:
            try:
                if e.find(class_="label-title").text == "Yönetmen:":
                    self.result["director"] = e.find(class_="label").text
                elif e.find(class_="label-title").text == "Yapımı:":
                    self.result["year"] = e.find("a").text
            except:
                pass


        self.result["name"] = content.find("h1").text
        # self.result["year"] = int(_info[6].find("a").text)
        # self.result["director"] = _info[4].find("a").text

        _showPosterTpl = BeautifulSoup(content.find(id="showPosterTpl").text, "html.parser")
        picURL = _showPosterTpl.find(class_="poster").get("src")

        self.pic = BytesIO(requests.get(picURL).content)

# print(FetchData("https://www.sinemalar.com/film/593/yuzuklerin-efendisi-3-kralin-donusu").picURL)

