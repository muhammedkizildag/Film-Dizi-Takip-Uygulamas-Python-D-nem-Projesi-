import requests
from bs4 import BeautifulSoup



class SearchData():
    def __init__(self, query):
        response = requests.get(f"https://www.sinemalar.com/ajax/search/autocomplete/?query={query}")

        content = BeautifulSoup(response.content, "html.parser").find_all("li")

        self.results = []

        for e in content:
            if e.find_all("span")[len(e.find_all("span"))-1].text != "Film" and e.find_all("span")[len(e.find_all("span"))-1].text != "Dizi":
                break

            dict = {"Name": e.find("a").get_text(strip=True, separator="/").split("/")[0],
                    "Type" : e.find_all("span")[len(e.find_all("span"))-1].text,
                    "PicURL": e.find("img").get("src")
                    }
            self.results.append(dict)




class FetchData():


    def __init__(self, URL):
        response = requests.get(URL)
        content = BeautifulSoup(response.content, "html.parser")

        _info = content.find_all(class_="info-group")

        self.result = {}
        self.result["name"] = content.find("h1").text
        self.result["year"] = int(_info[6].find("a").text)
        self.result["director"] = _info[4].find("a").text

        _showPosterTpl = BeautifulSoup(content.find(id="showPosterTpl").text, "html.parser")
        self.picURL = _showPosterTpl.find(class_="poster").get("src")



# print(FetchData("https://www.sinemalar.com/film/593/yuzuklerin-efendisi-3-kralin-donusu").pic)







