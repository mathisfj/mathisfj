##Modules
from tkinter import *
import numpy as np
import random as r
import os
##Image
link1='C:/Users/33760/Documents/Daudet/Démineur/bombe.ico'
link2='C:/Users/33760/Documents/Daudet/Démineur/Case.png'
link3='C:/Users/33760/Documents/Daudet/Démineur/Case vide.png'
link4='C:/Users/33760/Documents/Daudet/Démineur/drapeau.png'
link5='C:/Users/33760/Documents/Daudet/Démineur/bombe.png'
link6='C:/Users/33760/Documents/Daudet/Démineur/perdu.png'
link7='C:/Users/33760/Documents/Daudet/Démineur/win.png'
link8='C:/Users/33760/Documents/Daudet/Démineur/num/1.png'
link9='C:/Users/33760/Documents/Daudet/Démineur/num/2.png'
link10='C:/Users/33760/Documents/Daudet/Démineur/num/3.png'
link11='C:/Users/33760/Documents/Daudet/Démineur/num/4.png'
link12='C:/Users/33760/Documents/Daudet/Démineur/num/5.png'
link13='C:/Users/33760/Documents/Daudet/Démineur/num/6.png'
link14='C:/Users/33760/Documents/Daudet/Démineur/num/7.png'
link15='C:/Users/33760/Documents/Daudet/Démineur/num/8.png'
##Variables
nb_cases=0
taille=nb_cases*20
nb_bombe=0
a_voir=nb_cases**2-nb_bombe
lst_drapeau=[]
lst_bombe=[]
lst_boutons=[]
cases_vides=[]
##Interface
fenetre=Tk()
fenetre.title("Démineur")
fenetre.geometry("720x720")
fenetre.minsize(500,500)
fenetre.maxsize(1920,1080)
fenetre.iconbitmap(link1)
fenetre.config(background='red')
canvas=Canvas(fenetre,bg='black',highlightthickness=0)

##Photo
case=PhotoImage(file=link2)
case_vide=PhotoImage(file=link3)
drapeau=PhotoImage(file=link4)
bombe=PhotoImage(file=link5)
perdu=PhotoImage(file=link6)
win=PhotoImage(file=link7)
un=PhotoImage(file=link8)
deux=PhotoImage(file=link9)
trois=PhotoImage(file=link10)
quatre=PhotoImage(file=link11)
cinq=PhotoImage(file=link12)
six=PhotoImage(file=link13)
sept=PhotoImage(file=link14)
huit=PhotoImage(file=link15)
##Niveaux
def Debutant():
    global nb_bombe
    global a_voir
    global taille
    global nb_cases
    global canvas
    global terrain
    global lst_drapeau
    global lst_bombe
    nb_bombe = 20
    nb_cases = 15
    taille = nb_cases * 20
    lst_drapeau=[]
    lst_bombe=[]
    lst_boutons=[]
    cases_vides=[]
    lst_drapeau=[]
    toplevel = Toplevel(fenetre,bg='red')
    toplevel.title('Debutant')
    toplevel.iconbitmap(link1)
    toplevel.geometry('1920x1080')
    canvas = Canvas(toplevel, width = taille, height = taille, bg = 'grey',highlightthickness=0)
    canvas.pack(expand=YES)
    label = Label(toplevel, text='Pour gagner placer un drapeau sur chaque bombe', font=('Bahnschrift SemiBold',30),fg='red').pack(side=TOP,fill=X)
    terrain,lst_bombe=grille(nb_cases,nb_bombe)
    champ(terrain)
    damier(taille)
    canvas.bind("<Button-3>",click_droit)
    canvas.bind("<Button-2>",click_molette)
    canvas.bind("<Button-1>", click_gauche)


def Intermediaire():
    global nb_bombe
    global a_voir
    global taille
    global nb_cases
    global canvas
    global terrain
    global lst_drapeau
    global lst_bombe
    nb_bombe = 70
    nb_cases = 25
    taille = nb_cases * 20
    lst_drapeau=[]
    lst_bombe=[]
    lst_boutons=[]
    cases_vides=[]
    lst_drapeau=[]
    toplevel = Toplevel(fenetre,bg='red')
    toplevel.title('Intermédiaire')
    toplevel.iconbitmap(link1)
    toplevel.geometry('1920x1080')
    canvas = Canvas(toplevel, width = taille, height = taille, bg = 'grey',highlightthickness=0)
    canvas.pack(expand=YES)
    label = Label(toplevel, text='Pour gagner placer un drapeau sur chaque bombe', font=('Bahnschrift SemiBold',30),fg='red').pack(side=TOP,fill=X)
    terrain,lst_bombe=grille(nb_cases,nb_bombe)
    champ(terrain)
    case_non_ouverte(taille)
    damier(taille)
    canvas.bind("<Button-3>",click_droit)
    canvas.bind("<Button-2>",click_molette)
    canvas.bind("<Button-1>", click_gauche)

def Expert():
    global nb_bombe
    global a_voir
    global taille
    global nb_cases
    global canvas
    global terrain
    global lst_drapeau
    global lst_bombe
    nb_bombe = 150
    nb_cases = 50
    taille = nb_cases * 20
    lst_drapeau=[]
    lst_bombe=[]
    lst_boutons=[]
    cases_vides=[]
    lst_drapeau=[]
    toplevel = Toplevel(fenetre,bg='red')
    toplevel.title('Expert')
    toplevel.iconbitmap(link1)
    toplevel.geometry('1920x1080')
    canvas = Canvas(toplevel, width = taille, height = taille, bg = 'grey',highlightthickness=0)
    canvas.pack(expand=YES)
    label = Label(toplevel, text='Pour gagner placer un drapeau sur chaque bombe', font=('Bahnschrift SemiBold',30),fg='red').pack(side=TOP,fill=X)
    terrain,lst_bombe=grille(nb_cases,nb_bombe)
    champ(terrain)
    case_non_ouverte(taille)
    damier(taille)
    canvas.bind("<Button-3>",click_droit)
    canvas.bind("<Button-2>",click_molette)
    canvas.bind("<Button-1>", click_gauche)

##Bouton
frame=Frame(fenetre,bg='red')
frame.pack(expand=YES,fill=X)
btn1 = Button(frame, text = 'Débutant',bg='white',font=('Bahnschrift SemiBold',30), activebackground = 'black',cursor = 'cross',command = Debutant)
btn2 = Button(frame, text = 'Intermédiaire',bg='white',font=('Bahnschrift SemiBold',30),activebackground = 'black',cursor = 'cross',command = Intermediaire)
btn3 = Button(frame, text = 'Expert', font=('Bahnschrift SemiBold',30),bg='white',activebackground = 'black',cursor = 'cross', command = Expert)
btn1.pack(pady=20,fill=X)
btn2.pack(pady=20,fill=X)
btn3.pack(pady=20,fill=X)
##Jeu
def grille(n=nb_cases,nombre_bombe=nb_bombe):
    terrain=np.zeros((n,n))
    lst_bombe=[]
    i=0
    while i<=nombre_bombe:
        x=r.randint(0,n-1)
        y=r.randint(0,n-1)
        if terrain[y,x]!=10:
            terrain[y,x]=10
            lst_bombe.append((y,x))
            voisins=[[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
            for v in voisins:
                x0=x+v[0]
                y0=y+v[1]
                if 0<=x0<n and 0<=y0<n:
                    if terrain[y0,x0]!=10:
                        terrain[y0,x0]+=1
        i+=1
    return (terrain,lst_bombe)

##Création damier
def ligne_verticale(taille=taille):
    x = 0
    while x!=taille:
        canvas.create_line(x,0,x,taille,width=2,fill='black')
        x+=20

def ligne_horizontale(taille=taille):
    y = 0
    while y!=taille:
        canvas.create_line(0,y,taille,y,width=2,fill='black')
        y+=20

def damier(taille=taille):
    ligne_verticale(taille)
    ligne_horizontale(taille)

def case_non_ouverte(taille=taille):
    for x in range (nb_cases):
        L=[]
        for y in range(nb_cases):
            id=canvas.create_image(10+20*x,10+20*y,image=case)
            L.append(id)
        lst_boutons.append(L)

def champ(m):
    lst = ['Blue', 'Red', 'Green', 'Orange', 'Cyan', 'Purple', 'Brown', 'Peru']
    for i in range (nb_cases):
        for j in range(nb_cases):
            k=int(m[i,j])
            if m[i,j] != 0 and m[i,j]!=10:
                color = lst[k-1]
                canvas.create_text((10+20*i,10+20*j), text='{0:d}'.format(k), width = 20, font = 'Arial', fill = color)
            else :
                if m[i,j]==10:
                    canvas.create_image(10+20*i,10+20*j,image=bombe)
            if k==0:
                canvas.create_image(10+20*i,10+20*j,image=case_vide)





##Défaite
def Defaite():
    toplevel1 = Toplevel(fenetre)
    toplevel1.title('Démineur')
    toplevel1.geometry('720x720')
    toplevel1.iconbitmap(link1)
    canvas2= Canvas(toplevel1, width = 720, height = 720, bg = 'white', bd=1)
    canvas2.create_image(360,360,image=perdu)
    canvas2.pack(expand=YES)

def recherche_bombe(lst_bombe):
    for v in lst_bombe:
        x=v[0]
        y=v[1]
        canvas.create_image(10+20*x,10+20*y,image=bombe)
##Victoire
def comparer(l1,l2):
    compteur = 0
    n = len(l1)
    for i in range(n):
        for j in range(n):
            if l1[i] == l2[j]:
                compteur += 1
    if compteur == n:
        return True
    return False

def victoire(l1,l2):
    if len(lst_drapeau)==len(lst_bombe):
        l = []
        for X in lst_drapeau:
            x,y = X[1], X[2]
            l.append((x,y))
        if comparer(lst_bombe,l):
            gagne()

def gagne():
    toplevel2 = Toplevel(fenetre)
    toplevel2.title('Démineur')
    toplevel2.geometry('720x720')
    toplevel2.iconbitmap(link1)
    canvas3=Canvas(toplevel2, width = 700, height = 700, bg = 'black')
    canvas3.create_image(350,350,image=win)
    canvas3.pack(expand=YES)
##Clics
def recherche_voisine(X,Y):
    voisins=[[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[1,-1],[-1,1]]
    list=[1,2,3,4,5,6,7,8]
    l=[un,deux,trois,quatre,cinq,six,sept,huit]
    deja_vu=[]
    n=nb_cases
    voisines=[]
    for v in voisins:
        x,y=X+v[0],Y+v[1]
        if 0<=x<n and 0<=y<n:
            voisines.append((x,y))
            if terrain[y,x]==0:
                canvas.create_image(20*x+10,20*y+10,image=case_vide)
            for i in range(len(voisines)):
                recherche_voisine(voisines[i][0],voisines[i][0])


def click_gauche(event):
    x=event.x
    y=event.y
    if x%20==10:
        x=x
    else:
        x=x-(x%20)+10
    if y%20==10:
        y=y
    else:
        y=y-(y%20)+10
    x0=x//20
    y0=y//20
    if (x0,y0) in lst_bombe:
        canvas.create_image(x,y,image=bombe)
        recherche_bombe(lst_bombe)
        Defaite()
    lst = [un,deux,trois,quatre,cinq,six,sept,huit]
    list=[1,2,3,4,5,6,7,8]
    for i in range(len(list)):
        if terrain[x0,y0]==list[i]:
            canvas.create_image(x,y,image=lst[i])
    if terrain[x0,y0]==0:
        canvas.create_image(x,y,image=case_vide)
        recherche_voisine(x0,y0)









def click_droit(event):
    x = event.x
    y = event.y
    if x%20==10:
        x=x
    else:
        x=x-(x%20)+10
    if y%20==10:
        y=y
    else:
        y=y-(y%20)+10
    x0=x//20
    y0=y//20
    id=canvas.create_image(x,y,image=drapeau)
    if (y0,x0) not in lst_drapeau:
        lst_drapeau.append([id,x0,y0])
    victoire(lst_drapeau,lst_bombe)

def click_molette():
    X,Y = event.x//20, event.y//20
    x,y = 10+20*X, 10+20*Y
    for k in lst_drapeau:
        if (x,y) == (k[1],k[2]):
            id = k[0]
            cnv.delete(id)
            lst_drapeau.remove([id,x,y])


##Afficher
fenetre.mainloop()









