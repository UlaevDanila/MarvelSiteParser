from bs4 import BeautifulSoup
import requests
import re

url = "https://www.marvel.com/characters"

characters = requests.get(url)

filteredCharacters = []
allCharacters = []

soup = BeautifulSoup(characters.text, "html.parser")

allCharacters = soup.find_all("div", class_="card-body is-sliding")


for data in allCharacters:
    if data.find("p", class_="card-body__headline") is not None:
        temp = data.find("p", class_="card-body__headline")
        temp = re.findall(r'>(.+?)<', str(temp))
        filteredCharacters.append(temp[0])

print(filteredCharacters)