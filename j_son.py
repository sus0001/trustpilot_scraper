# cfrom base64 import encode
import json
import requests
import pandas as pd

jsondata = requests.get("https://api.cardacity.io/assets?page=1").content
# json_data = json.loads(r)
# print(json_data['दैनिक मूल्यहरु - वि.सं. जेठ २३, २०७९']['Unit'])

'''write_json = True
if write_json:
    with open('carda.json', 'wb') as f:
        f.write(jsondata)
else:
    with open('carda.json', encoding='utf-8') as file:
        data = json.load(file)'''


api_urls = [f"https://api.cardacity.io/assets?page={i}" for i in range(1, 1108)]

carda_urls = []
img_urls = []
names = []
lats = []
lngs = []
populations = []
lngs = []
countries = []
continents = []

        
for j in range(0, 11111):
    try:
        for url in api_urls:           
            carda_json_data = json.loads(requests.get(url).content)   
        
            carda_url = f"https://www.carda.city/collection/{carda_json_data['items'][j]['id']}"
            img_url = carda_json_data['items'][j]['imageUrl']
            name = carda_json_data['items'][j]['city']['name']
            lat = carda_json_data['items'][j]['city']['lat']
            lng = carda_json_data['items'][j]['city']['lng']
            population = carda_json_data['items'][j]['city']['population']
            country = carda_json_data['items'][j]['city']['country']['name']
            continent = carda_json_data['items'][j]['city']['country']['continent']
            carda_urls.append(carda_url), img_urls.append(img_url), names.append(name), lats.append(lat), lngs.append(lng), populations.append(population), countries.append(country), continents.append(continent)
    except IndexError:
        break

    

d = {"Name": names, "Country": countries, "Continent": continents, "Latitude": lats, "Longitude": lngs, "Population": populations, "NFT URL": carda_urls, "Image URL": img_urls}
df = pd.DataFrame(data=d)
df.to_excel("Carda City NFT Database.xlsx", index=False)