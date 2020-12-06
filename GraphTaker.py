import requests
import time

def search (dico, URL):
    file = open("Borsonaro.txt", "a")
    for code in dico:
        page = requests.get(URL + code)
        file.write(time.strftime("%H:%M" + '-'))
        file.write(code + '-')
        print(str(page.text).split('<span class="c-instrument c-instrument--last" data-ist-last>')[-1].split(
            '</span><span class="c-faceplate__settle">')[0])
        file.write(str(page.text).split('<span class="c-instrument c-instrument--last" data-ist-last>')[-1].split(
            '</span><span class="c-faceplate__settle">')[0] + '\n')
    file.close()


code_Action_EPA = ['PROL', 'METEX', 'ONXEO', 'AUB', 'CRI', 'FALG', 'CGG', 'ORA', 'ORP', 'WLN', 'AIR']
code_Action_IT = ['AMP']
code_Action_US = ['AAPL']

horBegin = 900
horEndin = 1840

file = open("Borsonaro.txt", "a")
file.write('\n')
file.write("Cours du " + time.strftime("%d/%m/%y")+'\n'+'\n')
file.close()
while (1):
    file = open("Borsonaro.txt", "a")
    horaire = time.strftime("%H:%M")
    heureH = horaire.split(':')[0]
    heureM = horaire.split(':')[1]
    horaire = int(heureH + heureM)

    if horaire>=horBegin and horaire<=horEndin :
        search(code_Action_EPA,'https://www.boursorama.com/cours/1rP')
        search(code_Action_IT,'https://www.boursorama.com/cours/1g')
        search(code_Action_US,'https://www.boursorama.com/cours/')

        #for code in code_Action_EPA:
            #page = requests.get('https://www.boursorama.com/cours/1rP'+code)
            #file.write(time.strftime("%H:%M" +'-'))
            #file.write(code + '-')
            #print(str(page.text).split('<span class="c-instrument c-instrument--last" data-ist-last>')[-1].split('</span><span class="c-faceplate__settle">')[0])
            #file.write(str(page.text).split('<span class="c-instrument c-instrument--last" data-ist-last>')[-1].split('</span><span class="c-faceplate__settle">')[0] +'\n' )
        #file.close()
        time.sleep()
    else:
        break


file.close()








# # On importe Tkinter
# from tkinter import *
#
# # On crée une fenêtre, racine de notre interface
#
# fenetre = Tk()
# # fenetre1 = Tk()
#
# # On crée un label
# # Note : le premier paramètre passé au constructeur de Label est notre
# # interface racine
#
# champ_label = Label(fenetre, text="Tess Tass Toss !")
# # bouton_liste = Button(fenetre, text="Afficher", command=callback)
#
# var_case = IntVar()
# case = Checkbutton(fenetre, text="Airbus", variable=var_case)
# var_case.get()
# liste = Listbox(fenetre)
# liste.insert(END, "Airbus")
# liste.insert(END, "Amplifon")
# liste.insert(END, "Apple")
# liste.insert(END, "Orange")
# liste.insert(END, "Worldline")
# On affiche le label dans la fenêtre
























#
#
# champ_label.pack()
# case.pack()
#
# # liste.pack()
# # bouton_liste.pack()
#
# # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
# fenetre.mainloop()
#
#
#
# #
# # definir URL - code bourse EPA:XXX on recupere le XXX
# #
# # On recupere la valeur sur site
# # Recuperation de page html
# # transfert to string
# # decode utf_
# # split via delimiteur
# #
# # on affcihe les données dans le graph
#
