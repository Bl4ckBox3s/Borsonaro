import requests
import time


# Initialisation d'une fonction search qui prend en paramètres une URL et un code présent dans différents dictionnaires
# On récupère la page nous intéréssant via $page puis l'on découpe le html afin de récupérer la valeur recherchée 
def search (dico, URL):
    for code in dico:
        page = requests.get(URL + code)
        print(time.strftime("%H:%M" + '-' + code + '-' + str(page.text).split('<span class="c-instrument c-instrument--last" data-ist-last>')[-1].split('</span><span class="c-faceplate__settle">')[0]))

# Initialisation des dictionnaires correspondant à une URL qui lui est propre
code_Action_EPA = ['PROL', 'METEX', 'ONXEO', 'AUB', 'CRI', 'FALG', 'CGG', 'ORA', 'ORP', 'WLN', 'AIR']
code_Action_IT = ['AMP']
code_Action_US = ['AAPL']

# On définit une variable d'heure de  début et de fin
horBegin = 830
horEndin = 1730

# On effectue la comparaison entre nos $ de temps et l'heure
while (1):
    horaire = time.strftime("%H:%M")
    heureH = horaire.split(':')[0]
    heureM = horaire.split(':')[1]
    horaire = int(heureH + heureM)

#On vérifie que nous sommes dans la bonne tranche horaire
# le else nous permet de sortir de la boucle si la tranche horaire n'est pas respectée
# le exit est nécessaire pour automatiser ensuite le lancement du script via crontab
    if horaire>=horBegin and horaire<=horEndin :
        search(code_Action_EPA,'https://www.boursorama.com/cours/1rP')
        search(code_Action_IT,'https://www.boursorama.com/cours/1g')
        search(code_Action_US,'https://www.boursorama.com/cours/')
        exit(1)
    else:
        break


# Commandes crontab afin de gérer l'automatisation.
#30 8 * * 1-5  python3 /home/pi/Documents/Borsonaro/Borsonaro/extract.py>>/home/pi/Documents/Borsonaro/Borsonaro/$(date +\%d\%m\%Y).txt    -> tous les jours de la semaine à partir de 8h30
#*/10 * * * 1-5  python3 /home/pi/Documents/Borsonaro/Borsonaro/extract.py>>/home/pi/Documents/Borsonaro/Borsonaro/$(date +\%d\%m\%Y).txt  -> toutes les 10"




# on extrait les données
# on affiche les différents ID codes 
# on affiche les données récupérées dans un graph

