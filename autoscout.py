import json
import requests
from bs4 import BeautifulSoup


base_url = "https://www.autoscout24.ro"

query = input(
    "Introduceti link-ul: ")

query = query.replace("https://www.autoscout24.ro","").replace("page=2", "page={}")

HEADERS = {
    'User-Agemt': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70 (Edition std-1)'
}
args = []
for x in range(1, 21):
  response = requests.get(base_url + query.format(x), headers=HEADERS)

  html = response.text

  soup = BeautifulSoup(html, 'html.parser')

  elements = soup.find_all("article", {
                           "class": "cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__ppamD"})

  urls = []
  for element in elements:
    url = element.select_one(
        "div.ListItem_wrapper__J_a_C div.ListItem_header__uPzec a")["href"]
    urls.append(base_url + url)

  for url in urls:
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    try:
      mark = soup.find("span", {"class": "css-1mhe8d errr7t00"}).text
    except Exception:
      mark = "Not found"
    try:
      model = soup.find("div", {"class": "css-l08njs"}).text
    except Exception:
      model = " "
    try:
      fuelType = soup.find("div", {"class": "StageArea_container__YuNIp"}).find("div", {
          "class": "StageArea_overviewContainer__dElor"}).find_all("div", {
          "class": "VehicleOverview_itemContainer__Ol37r"})[3].find("div", {"class": "VehicleOverview_itemText__V1yKT"}).text
    except Exception:
        fuelType = "Not found"
    try:
      color = soup.find("div", {"data-cy": "color-section"}
                        ).find("dd", {"class": "css-uvt9sy"}).text
    except Exception:
      color = "Not found"
    try:
      km = soup.find("div", {"data-cy": "listing-history-section"}
                     ).find_all("dd", {"class": "css-uvt9sy"})[0].text
    except Exception:
      km = "Not found"
    try:
      years = soup.find("div", {"data-cy": "listing-history-section"}
                        ).find_all("dd", {"class": "css-uvt9sy"})[1].text
    except Exception:
      years = "Not found"
    try:
      country = soup.find("div", {"class": "StageArea_container__YuNIp"}).find("div", {
          "class": "StageArea_informationContainer__VaFP8"}).find("a", {"class": "scr-link css-4uy6qb"}).text
    except Exception:
        country = "Not found"
    try:
      price = soup.find("div", {"class": "StageArea_container__YuNIp"}).find("div", {"class": "StageArea_informationContainer__VaFP8"}).find(
          "div", {"class": "css-1371dt3"}).find("span", {"class": "StandardPrice_price__X_zzU"}).text.strip().replace(",-1", "").replace(",-", "")
    except Exception:
      price = "Not found"
    try:
      comfort = soup.find("div", {"data-cy": "equipment-section"}).find("div", {"class": "DetailsSection_detailsSection__2cTru"}).find(
          "div", {"class": "DetailsSection_childrenSection__NQLD7"}).find("div", {"class": "DetailsSection_autoMargin__LCLCW"}).find_all("dd", {"class": "css-p6jua1"})[0].text
    except Exception:
      comfort = "Not found"
    try:
      media = soup.find("div", {"data-cy": "equipment-section"}).find("div", {"class": "DetailsSection_detailsSection__2cTru"}).find(
          "div", {"class": "DetailsSection_childrenSection__NQLD7"}).find("div", {"class": "DetailsSection_autoMargin__LCLCW"}).find_all("dd", {"class": "css-p6jua1"})[1].text
    except Exception:
      media = "Not found"
    try:
      security = soup.find("div", {"data-cy": "equipment-section"}).find("div", {"class": "DetailsSection_detailsSection__2cTru"}).find(
          "div", {"class": "DetailsSection_childrenSection__NQLD7"}).find("div", {"class": "DetailsSection_autoMargin__LCLCW"}).find_all("dd", {"class": "css-p6jua1"})[2].text
    except Exception:
      security = "Not found"
    try:
      option = soup.find("div", {"data-cy": "equipment-section"}).find("div", {"class": "DetailsSection_detailsSection__2cTru"}).find(
          "div", {"class": "DetailsSection_childrenSection__NQLD7"}).find("div", {"class": "DetailsSection_autoMargin__LCLCW"}).find_all("dd", {"class": "css-p6jua1"})[3].text
    except Exception:
      option = "Not found"
    href = url
    args.append(
        {
            "Marca": mark,
            "Model": model,
            "Combustibil": fuelType,
            "Culoare": color,
            "Kilometraj": km,
            "Tara": country,
            "Prima înmatriculare": years,
            "Pret": price,
            "link": href,
            "Confort": comfort,
            "Divertisment/Media": media,
            "Securitate": security,
            "Optiuni": option
        }
    )
  print("Status message: page = {}".format(x))
with open("autoscout.json", "w", encoding="utf8") as f:
    json.dump(args, f)

print("result: ", len(args))

with open("autoscout.json", "r", encoding="utf8") as f:
  data = json.load(f)

print(len(data))
