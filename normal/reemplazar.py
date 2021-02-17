import os

ParaReemplazar = ['Carcaj de mediodía', 'Centinela invisible', 'Filo del Robahechizos', 'Hoja granizo', 'Cuchillo Ámbar', 'El Coleccionista', 'Sombrero mortífero de Rabadon', 'Fuerza del Viento', 'Ángel Guardián', 'Filo del infinito', 'Recordatorio mortal', 'Grebas de berserker', 'Punteras de acero revestidas', 'Botas del hechicero', 'Látigo férreo', 'Bebedor de sangre', 'Guantelete de Sterak', 'Apariencia espiritual', 'Sierraespada Quimopunk', 'Fuerza de la trinidad', 'Maldición del liche', 'Bastón del Vacío', 'Relicario de los Solari de Hierro', 'Promesa del caballero', 'Égida de fuego solar', 'Cota de espinas', 'Armadura pétrea', 'Angustia de Liandry', 'Báculo del arcángel', 'Pebetero ardiente', 'Báculo de agua fluyente', 'Gemaluz', 'Cercenador divino', 'Danza de la muerte', 'Puñal serrado', 'Al filo de la Cordura', 'Velo de la banshee', 'Cuchilla oscura', 'Ceniza de Bami', 'Agrietador', 'Matakrakens']

ReemplazarPor = ['Carcaj de mediodía', 'Centinela invisible', 'Filo del Robahechizos', 'Hoja granizo', 'Cuchillo Ámbar', 'El Coleccionista', 'Sombrero mortífero de Rabadon', 'Fuerza del Viento', 'Ángel Guardián', 'Filo del infinito', 'Recordatorio mortal', 'Grebas de berserker', 'Punteras de acero revestidas', 'Botas del hechicero', 'Látigo férreo', 'Bebedor de sangre', 'Guantelete de Sterak', 'Apariencia espiritual', 'Sierraespada Quimopunk', 'Fuerza de la trinidad', 'Maldición del liche', 'Báculo del vacío', 'Relicario de los Solari de Hierro', 'Promesa del caballero', 'Égida de fuego solar', 'Cota de espinas', 'Armadura pétrea', 'Angustia de Liandry', 'Báculo del arcángel', 'Pebetero ardiente', 'Báculo de agua fluyente', 'Gemaluz', 'Cercenador divino', 'Danza de la muerte', 'Puñal serrado', 'Al filo de la Cordura', 'Velo de la banshee', 'Cuchilla oscura', 'Ceniza de Bami', 'Agrietador', 'Matakrakens']

for champ in os.listdir('.'):
  print(champ)
  original = open(champ, 'r')
  reemplazo = original.read()
  for i in range(len(ParaReemplazar)):
    reemplazo = reemplazo.replace(ParaReemplazar[i], ReemplazarPor[i])
  original.close()
  original = open(champ, 'w')
  original.write(reemplazo)
  original.truncate()
  original.close()