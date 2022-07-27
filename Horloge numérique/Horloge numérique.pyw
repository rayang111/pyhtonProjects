#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Importation des modules requis (et vérification de l'installation de pillow)
import time
from time import strftime 
from tkinter import *
import tkinter.filedialog
import tkinter
import tkinter.font as tkFont
from turtle import *
import turtle
try:
    from PIL import Image, ImageTk
except ModuleNotFoundError:
    print(' Erreur, module manquant : Vous n\'avez pas installé pillow (PIL). Pour utilliser ce logiciel vous devez l\'installer grâce à PIP sur le terminal de votre ordinateur ou alors sur le site web pypi.org/project/Pillow/')
    tkinter.messagebox.showerror('Module manquant','Erreur : Vous n\'avez pas installé pillow (PIL). \nPour utilliser ce logiciel vous devez l\'installer grâce à PIP sur le terminal de votre ordinateur ou alors sur leur site web pypi.org/project/Pillow/')
    quit()
import os

#Fonction qui permet de quitter le programme entièrement
def quitter():
    if tkinter.messagebox.askyesno('Quitter ?','Voulez vous vraiment quitter ?', default = 'no'):  #Pour savoir si l'utilisateur est sûr de quitter 
        window.destroy()
        window.quit()
        try:
            window2.destroy()
            window2.quit()
        except NameError:
            pass
        except tkinter.TclError:
            pass
        try:
            window3.destroy()
            window3.quit()
        except NameError:
            pass
        except tkinter.TclError:
            pass
        try:
            window4.destroy()
            window4.quit()
        except NameError:
            pass
        except tkinter.TclError:
            pass        
    else:
        pass
    
#Fonction permettant de créer et d'afficher les dessins
def dessin():
    global window3
    try:
        launchbutton.config(state = 'disabled')
        window3 = Tk()
        window3.protocol("WM_DELETE_WINDOW", fermerdessin)
        window3.title('Dessin')
        window3.resizable(False,False)
        can = Canvas(window3, width=800, height=600)
        bouton3 = Button(window3, text="Fermer", command=fermerdessin, overrelief = 'groove')
        turtle_screen = turtle.TurtleScreen(can)
        turtle_screen.bgcolor("black")
        can.pack()
        bouton3.pack()
        Pen = RawTurtle(turtle_screen)
        Pen.clear()
        Pen.hideturtle()
        #Dessin du pologone complexe
        Pen.speed(100)
        Pen.goto(0,0)
        Pen.color('red')
        Pen.down()
        for y in range(1,75):
            Pen.right(40)
            Pen.forward(100)
            Pen.right(250)
            Pen.forward(50)
            Pen.left(25)
            Pen.forward(60)
        Pen.up()
        Pen.clear()
        #Dessin du prisme
        Pen.home()
        Pen.down()
        #Prisme : création du prisme
        Pen.color('white')
        Pen.width(3)
        Pen.right(60)
        Pen.forward(100)
        Pen.right(120)
        Pen.forward(100)
        Pen.right(120)
        Pen.forward(100)
        Pen.up()
        Pen.width(1)
        Pen.home()
        #Prisme : création de la lumière
        Pen.goto(-400,-70)
        Pen.left(6)
        Pen.down()
        Pen.forward(380)
        Pen.right(9)
        #Prisme : décomposition de la lumière
        Pen.begin_fill()
        Pen.forward(40)
        Pen.right(60)
        Pen.forward(10)
        Pen.right(132)
        Pen.forward(43)
        Pen.end_fill()
        #Prisme : création de l'arc-en-ciel
        #( les instrutions répétées sont obligatoires dans ce cas là car pour chaque couleur il y a une personnalisation des parramètres (angle, distance, ...)
        #il sera plus diffcile de faire une fonction 
        Pen.right(167)
        Pen.forward(39)
        Pen.begin_fill()
        Pen.color('red')
        Pen.down()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(11)
        Pen.right(91.15)
        Pen.forward(446)
        Pen.end_fill()
        Pen.color('orange')
        Pen.up()
        Pen.right(180)
        Pen.down()
        Pen.begin_fill()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(11)
        Pen.right(91.15)
        Pen.forward(445)
        Pen.end_fill()
        Pen.up()
        Pen.color('yellow')
        Pen.right(180)
        Pen.down()
        Pen.begin_fill()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(11)
        Pen.right(91.15)
        Pen.forward(446)
        Pen.end_fill()
        Pen.up()
        Pen.color('green')
        Pen.right(180)
        Pen.down()
        Pen.begin_fill()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(11)
        Pen.right(91.15)
        Pen.forward(446)
        Pen.end_fill()
        Pen.up()
        Pen.color('blue')
        Pen.right(180)
        Pen.down()
        Pen.begin_fill()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(11)
        Pen.right(91.15)
        Pen.forward(446)
        Pen.end_fill()
        Pen.up()
        Pen.color('purple')
        Pen.right(180)
        Pen.down()
        Pen.begin_fill()
        Pen.forward(447)
        Pen.right(90)
        Pen.forward(10)
        Pen.right(91.15)
        Pen.forward(445)
        Pen.end_fill()
        Pen.up()         
        window3.mainloop()
    except tkinter.TclError:
        pass

#Fonction permetant de fermer la fenêtre des dessins    
def fermerdessin():
    launchbutton.config(state = 'normal')
    window3.destroy()
    
#Fonction gèrant la fenêtre à propos de l'horloge (texte du à propos inporté d'un fichier texte (.txt) pour éviter que le code soit trop long)
def about():
    global window2
    apropos = open('apropos.txt', "r", encoding='utf-8')
    window2 = Tk()
    window2.resizable(False,False)
    window2.title('A propos de l\'horloge')
    label2 = Label(window2, text='Bienvenue sur l\'Horloge numérique !', fg = 'red', font = ("Helvetica",18))
    fra2 = Frame(window2)
    fraText = Label(fra2, text=apropos.read(), font = ("Helvetica",10), relief = 'groove', bg = 'white')
    bouton2 = Button(window2, text="Fermer", command=window2.destroy, overrelief = 'groove')
    label2.pack()
    fra2.pack()
    fraText.pack()
    bouton2.pack()
    window2.mainloop()
#Fonction gèrant la visionneuse d'images, cette fonction ouvre une image et la place dans un canvas, ATTENTION : Il faut avoir le module pillow (PIL) pour que cela fonctionne
def openimg():
    global window4
    img = tkinter.filedialog.askopenfilename(filetypes=[('Images compatibles','*.png *.jpeg *.png')])
    imgname = ''
    for n in range(len(img)-1,1,-1):
        if img[n] != '/':
            imgname = img[n] + imgname
        else:
            break
    window4 = Tk()
    window4.resizable(False,False)
    window4.title('Visionneuse d\'images : ' + imgname)
    photo = ImageTk.PhotoImage(master = window4, file = img)
    canv = Canvas(window4,width = photo.width(), height = photo.height()) 
    canv.create_image(0,0, anchor = NW, image=photo)
    bouton3 = Button(window4, text="Fermer", command=window4.destroy, overrelief = 'groove')
    canv.pack()
    bouton3.pack()
    window4.mainloop()
    
#Fonction qui actualise l'horloge et la date du jour à chaque secondes)    
def actualisation():
    label.config(text = strftime('%H:%M:%S'))
    annee.config(text = str(time.localtime()[0]))
    mois.config(text = moisn)
    jour.config(text = str(time.localtime()[2]))
    jourl.config(text = daym)
    label.after(200,actualisation)

#Obtention du mois et du jour, "modification" du jour en anglais et abbrégé vers le nom de la journée complete et en français, "modication" du numéro du mois vers le nom du mois     
moisn = int(time.localtime()[1])
daym = time.ctime()[0:3]
num = [('Janvier',1),('Février',2),('Mars',3),('Avril',4),('Mai',5),('Juin',6),('Juillet',7),('Août',8),('Septembre',9),('Octobre',10),('Novembre',11),('Décembre',12)]
day = [('Mon','Lundi'),('Tue','Mardi'),('Wed','Mercredi'),('Thu','Jeudi'),('Fri','Vendredi'),('Sat','Samedi'),('Sun','Dimanche')]

#Boucle fesant la "modification" du jour et du mois
for i in num:
    if moisn == i[1]:
        moisn = i[0]
for i in day:
    if daym == i[0]:
        daym = i[1]
        
#Gestion de la fenêtre principale et mis en place de l'horloge et de l'actualisation de cette dernière
window = Tk()
window.title('Horloge numérique')
window.protocol("WM_DELETE_WINDOW", quitter)
window.resizable(False,False)
fra = Frame(window, relief = 'groove', borderwidth = 4, bg = 'white')
fra2 = Frame(fra, bg = 'white')
Horloge = Label(window, text='HORLOGE', fg = 'yellow', bg = 'brown', font = ("Times",25))
label = Label(fra, text=strftime('%H:%M:%S'), font = ("Helvetica", 50, 'bold'), bg = 'white')
annee = Label(fra2, text=str(time.localtime()[0]), fg = 'gray', font = ("Helvetica",18), bg = 'white')
mois = Label(fra2, text=moisn, fg = 'gray', font = ("Helvetica",18), bg = 'white')
jour = Label(fra2, text=str(time.localtime()[2]), fg = 'gray', font = ("Helvetica",18), bg = 'white')
jourl = Label(fra2, text=daym, fg = 'gray', font = ("Helvetica",18), bg = 'white')
aboutbutton = Button(window, text="A propos de l\'horloge", command=about, overrelief = 'groove')
openbutton = Button(window, text="Ouvrir une image", command=openimg, overrelief = 'groove')
launchbutton = Button(window, text="Lancer le dessin", command=dessin, overrelief = 'groove', state = 'normal')
quitbutton = Button(window, text="Quitter", command=quitter, overrelief = 'groove')
Horloge.pack()
fra.pack()
label.pack()
fra2.pack()
annee.pack(side = RIGHT)
mois.pack(side = RIGHT)
jour.pack(side = RIGHT)
jourl.pack(side = RIGHT)
aboutbutton.pack(side = LEFT)
openbutton.pack(side = LEFT)
launchbutton.pack(side = LEFT)
quitbutton.pack(side = RIGHT)    
actualisation()
window.mainloop()

