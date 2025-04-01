import requests
from bs4 import BeautifulSoup

test_url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=test_url)  #might need a headers field?

soup = BeautifulSoup(response.text, "html.parser")
span2 = soup.find(name="span", class_="aok-offscreen")
print(span2.getText().split("$")[1])
