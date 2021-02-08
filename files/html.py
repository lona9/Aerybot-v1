import os
import requests

foldername = 'files'

champs = ['aatrox', 'ahri', 'akali', 'alistar', 'amumu', 'anivia', 'annie', 'aphelios', 'ashe', 'aurelion sol', 'azir', 'bardo', 'blitzcrank', 'brand', 'braum', 'caitlyn', 'camille', 'cassiopeia', 'chogath', 'corki', 'darius', 'diana', 'drmundo', 'draven', 'ekko', 'elise', 'evelynn', 'ezreal', 'fiddlesticks', 'fiora', 'fizz', 'galio', 'gangplank', 'garen', 'gnar', 'gragas', 'graves', 'hecarim', 'heimerdinger', 'illaoi', 'irelia', 'ivern', 'janna', 'jarvaniv', 'jax', 'jayce', 'jhin', 'jinx', 'kaisa', 'kalista', 'karma', 'karthus', 'kassadin', 'katarina', 'kayle', 'kayn', 'kennen', 'khazix', 'kindred', 'kled', 'kogmaw', 'leblanc', 'leesin', 'leona', 'lillia', 'lissandra', 'lucian', 'lulu', 'lux', 'masteryi', 'malphite', 'malzahar', 'maokai', 'missfortune', 'mordekaiser', 'morgana', 'nami', 'nasus', 'nautilus', 'neeko', 'nidalee', 'nocturne', 'nunu', 'olaf', 'orianna', 'ornn', 'pantheon', 'poppy', 'pyke', 'qiyana', 'quinn', 'rakan', 'rammus', 'reksai', 'rell', 'renekton', 'rengar', 'riven', 'rumble', 'ryze', 'samira', 'sejuani', 'senna', 'seraphine', 'sett', 'shaco', 'shen', 'shyvana', 'singed', 'sion', 'sivir', 'skarner', 'sona', 'soraka', 'swain', 'sylas', 'syndra', 'tahmkench', 'taliyah', 'talon', 'taric', 'teemo', 'thresh', 'tristana', 'trundle', 'tryndamere', 'twistedfate', 'twitch', 'udyr', 'urgot', 'varus', 'vayne', 'veigar', 'velkoz', 'vi', 'viego', 'viktor', 'vladimir', 'volibear', 'warwick', 'wukong', 'xayah', 'xerath', 'xinzhao', 'yasuo', 'yone', 'yorick', 'yuumi', 'zac', 'zed', 'ziggs', 'zilean', 'zoe', 'zyra']

for url in urls:
    response = requests.get(url)
    with open(os.path.join(foldername,
                           url.split('/')[-2]), mode = 'wb') as file:
        file.write(response.content)