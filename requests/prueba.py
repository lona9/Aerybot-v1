import os
import requests
from bs4 import BeautifulSoup

nombres = []
for champ in os.listdir('files'):
  with open(os.path.join('files', champ)) as file:
    soup = BeautifulSoup(file, features='html5lib')
    nombre = soup.find('div', class_="iconsRow")
    print(nombre)
    break