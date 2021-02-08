import os
from bs4 import BeautifulSoup

nombres = []
# for champ in os.listdir('files'):
archivo = 'ahri.txt'
with open(os.path.join('files', archivo)) as file:
  soup = BeautifulSoup(file, features='html5lib')

  ## NOMBRE
  nombre = soup.find('meta', attrs={'name': "twitter:title"})
  nombre = str(nombre).replace('<meta content="Builds de ', '').replace(' - Objetos / Runas / Emparejamientos - League of Legends" name="twitter:title"/>', '')

  ## POSICIÓN
  posicion = soup.find('div', 'bannerSubtitle').contents
  posicion = "".join(posicion)
  posicion = posicion.strip()

  ## PORCENTAJE DE VICTORIAS
  victorias = soup.find('div', "pie-chart small", id="graphDD2").contents[0]
  victorias = "".join(victorias).strip()
  
  # ## RUNAS PRINCIPALES
  # opaqueprrunes = soup.find('table', "perksTableOverview").find_all('div', attrs={'style': "opacity: 0.2;"})
  # runasprincipales = []
  # for runa in range(len(opaqueprrunes)):
  #   primagenes = opaqueprrunes[runa].find('img', alt=True)
  #   alts = primagenes.get('alt')
  #   runasprincipales.append(alts)


  # ## RUNAS SECUNDARIAS
  # opaquesecrunes = soup.find('table', "perksTableOverview secondary").find_all('div', attrs={'style': "opacity: 0.2;"})
  # runassecundarias = []
  # for runa in range(len(opaquesecrunes)):
  #   secimagenes = opaquesecrunes[runa].find('img', alt=True)
  #   alts = secimagenes.get('alt')
  #   runassecundarias.append(alts)

  ## OBJETOS INICIALES Y FINALES
  objetos = soup.find_all('div', "championSpell small-margin")
  objinfin = []
  for obj in range(len(objetos)):
    imginfin = objetos[obj].find('img', alt=True)
    alts = imginfin.get('alt')
    objinfin.append(alts)
  x = len(objinfin) - 3
  objin = objinfin[:x]
  objin = ", ".join(objin)
  objfin = objinfin[-3:]
  objfin = ", ".join(objfin)

  ## BOTAS
  botas = soup.find_all('div', "championSpell")
  imgbotas = botas[-4].find('img', alt=True)
  botas = imgbotas.get('alt')

  ### OBJETOS PRINCIPALES
  principales = soup.find_all('div', "championSpell")
  objs = []
  for obj in range(len(principales)):
    imgprincipales = principales[obj].find('img', alt=True)
    principalts = imgprincipales.get('alt')
    objs.append(principalts)
  objpr = objs[-8:-4]
  objpr = " > ".join(objpr)

  texto = ("**{}** *(Normal)*\n**Posición:** *{}*\n**Porcentaje de victorias:** {}\n**Botas:** {}\n**Objetos iniciales:** {}\n**Objetos principales:** {}\n**Objetos finales:** {}".format(nombre, posicion, victorias, botas, objin, objpr, objfin))

  f = open(archivo, 'w+')
  f.write(texto)
  f.close()