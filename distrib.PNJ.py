###############################################################################

                          # Personnages non joueurs #

###############################################################################

import numpy as np
from tkinter import *
from random import randint

# Le but de ce code supposé être simple est d'automatiser la création de 
# personnages non joueurs (PNJ) de façon aléatoire. Chaque type de PNJ possède 
# des statistiques prédéterminées en fonction du rôle et de la puissance du
# personnage, mais avec des caractéristiques aléatoires. 

# L'objectif est d'obtenir en sortie de code une fiche de personnage simplifiée
# avec les caractéristiques correspondantes, accompagnée de quelques 
# informations rapides concernant les capacités du PNJ. 

# On va tenter de faire des "fonctions" que l'on pourra appeler pour obtenir la 
# fiche de personnage souhaitée. Un exemple : on souhaite obtenir la fiche 
# aléatoire d'un paysan, on rentre le mot "paysan" et obtient seulement cette 
# fiche. (et pas toutes les autres fiches des autres personnages). L'idée c'est
# d'avoir un code fini que l'on aura pas besoin de modifier à la source pour 
# obtenir ce que l'on veut. 

char = ['Force', 'Endurance', 'Dextérité', 'Perception', 'Savoir', 
        'Santé Mentale', 'Pouvoir', 'Discrétion', 'Charisme', 'Pilotage',
        'Artisanat']

color = ['red', 'green', 'yellow', 'blue', 'white', '#FFA500', 'magenta',
         '#C0C0C0', '#FFC0CB', 'cyan', '#582900']
         
         

' Paysan ' 

valpaysan = [randint(35,45), randint(40,50), randint(20,25), randint(15,25), 
             randint(10,20), randint(30,40), randint(0,5), randint(10,20),
             randint(15,30), randint(10,15), randint(40,60)]

pdvpaysan = randint(6,8)

nompaysan = ['Guethenot','Ropartz']

eqpaysan = ['Fourche', 'Dague', 'Sac de graines']

capapaysan = []

def paysan():
    w = Tk()
    
    app = PhotoImage(file = 'paysan.png')
    
    can = Canvas(w, width = 400, height = 800)
    can.create_image(0, 0, anchor = NW, image = app)
    can.pack(side = 'left')
    
    for i in range(np.size(char)):
        l = LabelFrame(w, text = char[i], font = 'bold', relief = 'groove', 
                       bg = color[i])
        l.pack(fill = 'both', expand = 'yes')
        Label(l, text = valpaysan[i], font = 'bold', bg = color[i]).pack()
    
    value = DoubleVar()
    scale = Scale(w, orient = 'horizontal', from_ = pdvpaysan, to = 0, 
                  label = 'Points de vie', font = 'bold', cursor = 'heart', 
                  relief = 'groove', variable = value)
    scale.set(pdvpaysan)
    scale.pack(fill = 'both', expand = 'yes')
    
    equip = LabelFrame(w, text = 'Équipements', font = 'bold')
    equip.pack(fill = 'both', expand = 'yes')
    Label(equip, text = eqpaysan).pack()
    
    capa = LabelFrame(w, text = 'Capacités', font = 'bold')
    capa.pack(fill = 'both', expand = 'yes')
    Label(capa, text = capapaysan).pack()
    
    w.title(nompaysan[randint(0,1)])
    
    w.mainloop()
    
    
' Ruvasejai ' 

valruva = [10, 10, 10, 60, 95, 80, 80, 50, 70, 10, 10]

pdvruva = 16

nomruva = ['Ruvasejai']

eqruva = []

caparuva = ['Omniscient']

def ruvasejai():
    w = Tk()
    
    app = PhotoImage(file = 'Ruva2.png')
    
    can = Canvas(w, width = 550, height = 800)
    can.create_image(0, 0, anchor = NW, image = app)
    can.pack(side = 'left')
    
    for i in range(np.size(char)):
        l = LabelFrame(w, text = char[i], font = 'bold', relief = 'groove', 
                       bg = color[i])
        l.pack(fill = 'both', expand = 'yes')
        Label(l, text = valruva[i], font = 'bold', bg = color[i]).pack()
    
    value = DoubleVar()
    scale = Scale(w, orient = 'horizontal', from_ = pdvruva, to = 0, 
                  label = 'Points de vie', font = 'bold', cursor = 'heart', 
                  relief = 'groove', variable = value)
    scale.set(pdvruva)
    scale.pack(fill = 'both', expand = 'yes')
    
    equip = LabelFrame(w, text = 'Équipements', font = 'bold')
    equip.pack(fill = 'both', expand = 'yes')
    Label(equip, text = eqruva).pack()
    
    capa = LabelFrame(w, text = 'Capacités', font = 'bold')
    capa.pack(fill = 'both', expand = 'yes')
    Label(capa, text = caparuva).pack()
    
    w.title(nomruva[0])
    
    w.mainloop()


' Izaroqui ' 

vali = [35, 40, 70, 80, 65, 75, 80, 80, 80, 60, 30]

pdvi= 38

nomi = ['Izaroqui']

eqi = []

capai = ['Effacement']

def izaroqui():
    w = Tk()
    
    app = PhotoImage(file = 'Iza1.png')
    
    can = Canvas(w, width = 600, height = 800)
    can.create_image(0, 0, anchor = NW, image = app)
    can.pack(side = 'left')
    
    for i in range(np.size(char)):
        l = LabelFrame(w, text = char[i], font = 'bold', relief = 'groove', 
                       bg = color[i])
        l.pack(fill = 'both', expand = 'yes')
        Label(l, text = vali[i], font = 'bold', bg = color[i]).pack()
    
    value = DoubleVar()
    scale = Scale(w, orient = 'horizontal', from_ = pdvi, to = 0, 
                  label = 'Points de vie', font = 'bold', cursor = 'heart', 
                  relief = 'groove', variable = value)
    scale.set(pdvi)
    scale.pack(fill = 'both', expand = 'yes')
    
    equip = LabelFrame(w, text = 'Équipements', font = 'bold')
    equip.pack(fill = 'both', expand = 'yes')
    Label(equip, text = eqi).pack()
    
    capa = LabelFrame(w, text = 'Capacités', font = 'bold')
    capa.pack(fill = 'both', expand = 'yes')
    Label(capa, text = capai).pack()
    
    w.title(nomi[0])
    
    w.mainloop()


' Ulrich Tesla ' 

valUT = [70, 80, 80, 50, 40, 90, 80, 40, 80, 60, 50]

pdvUT= 88

nomUT = ['Ulrich Tesla']

eqUT = ['Bâton Piézoélectrique']

capaUT = ['Imagination']

def ulrichtesla():
    w = Tk()
    
    app = PhotoImage(file = 'Ulrich.png')
    
    can = Canvas(w, width = 800, height = 800)
    can.create_image(0, 0, anchor = NW, image = app)
    can.pack(side = 'left')
    
    for i in range(np.size(char)):
        l = LabelFrame(w, text = char[i], font = 'bold', relief = 'groove', 
                       bg = color[i])
        l.pack(fill = 'both', expand = 'yes')
        Label(l, text = valUT[i], font = 'bold', bg = color[i]).pack()
    
    value = DoubleVar()
    scale = Scale(w, orient = 'horizontal', from_ = pdvUT, to = 0, 
                  label = 'Points de vie', font = 'bold', cursor = 'heart', 
                  relief = 'groove', variable = value)
    scale.set(pdvUT)
    scale.pack(fill = 'both', expand = 'yes')
    
    equip = LabelFrame(w, text = 'Équipements', font = 'bold')
    equip.pack(fill = 'both', expand = 'yes')
    Label(equip, text = eqUT).pack()
    
    capa = LabelFrame(w, text = 'Capacités', font = 'bold')
    capa.pack(fill = 'both', expand = 'yes')
    Label(capa, text = capaUT).pack()
    
    w.title(nomUT[0])
    
    w.mainloop()
    
    
' Jenbal '

valjenbal = [50, 60, 50, 50, 30, 60, 10, 40, 40, 80, 60]

pdvjenbal= 38

nomjenbal = ['Jenbal le Corsaire Noir']

eqjenbal = []

capajenbal = []

def jenbal():
    w = Tk()
    
    app = PhotoImage(file = 'Jenbal.png')
    
    can = Canvas(w, width = 600, height = 800)
    can.create_image(0, 0, anchor = NW, image = app)
    can.pack(side = 'left')
    
    for i in range(np.size(char)):
        l = LabelFrame(w, text = char[i], font = 'bold', relief = 'groove', 
                       bg = color[i])
        l.pack(fill = 'both', expand = 'yes')
        Label(l, text = valjenbal[i], font = 'bold', bg = color[i]).pack()
    
    value = DoubleVar()
    scale = Scale(w, orient = 'horizontal', from_ = pdvjenbal, to = 0, 
                  label = 'Points de vie', font = 'bold', cursor = 'heart', 
                  relief = 'groove', variable = value)
    scale.set(pdvjenbal)
    scale.pack(fill = 'both', expand = 'yes')
    
    equip = LabelFrame(w, text = 'Équipements', font = 'bold')
    equip.pack(fill = 'both', expand = 'yes')
    Label(equip, text = eqjenbal).pack()
    
    capa = LabelFrame(w, text = 'Capacités', font = 'bold')
    capa.pack(fill = 'both', expand = 'yes')
    Label(capa, text = capajenbal).pack()
    
    w.title(nomjenbal[0])
    
    w.mainloop()