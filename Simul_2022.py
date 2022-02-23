from tkinter import *

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        # on va chercher nos images pour les tours
        self.imgs={}
        self.imgs["tour"]=PhotoImage(file="tour.png")
        self.imgs["tour_trans"]=PhotoImage(file="tour_trans.png") # en semi_transparence
        self.creer_cadres()

    def creer_cadres(self):
        # fait en 2 sections
        # canevas 'principal'
        self.canevas=Canvas(self.root,width=600,height=400,bg="orange")
        self.canevas.create_rectangle(100,100,500,200,fill="green",tags=("fond","je suis fond"))
        self.canevas.pack(side=LEFT)
        # canvas pour les commandes et infos
        self.interface=Canvas(self.root,width=100,height=400,bg="lightblue")
        # j'utilise un radiobutton pour obtenir l'effet d'enfoncement jusqu'au placement de la tour
        self.btn_tour=Radiobutton(self.interface,image=self.imgs["tour"], text="tour",indicator=0,
                        value=1,command=self.creer_tour)

        self.btn_tour.pack()
        self.interface.pack(side=LEFT)

    # depuis l'interface on prepare le canevas pour suivre le curseur avec le fantome de la tour
    def creer_tour(self):
        # Motion pour promener le fantome
        self.canevas.bind("<Motion>",self.suivre_tour)
        # Button pour l'installer
        self.canevas.bind("<Button>",self.installer_tour)

    def suivre_tour(self,evt):
        x=evt.x
        y=evt.y
        # essentiellement on efface l'ancienne image et la redessine au neouvel endroit
        self.canevas.delete("tour_temp")
        self.canevas.create_image(x,y,image=self.imgs["tour_trans"],tags=("tour_temp",))

    def installer_tour(self,evt):
        x=evt.x
        y=evt.y
        # LA MAGIE S'OPERE ICI
        #  find_overlapping d'un rectangle
        #  retourne le id de tous les items dans un tuple
        # ici j'ai donc créer un rectangle autour de la position de souris
        listeitems=self.canevas.find_overlapping(evt.x-20,evt.y-20,evt.x+20,evt.y+20)
        if len(listeitems)==1: # sera vrai s'il n'y a que la tour_temp, donc un seul item
            self.canevas.create_image(x, y, image=self.imgs["tour"], tags=("tour", ))
            self.canevas.unbind("<Motion>")
            self.canevas.unbind("<Button>")
            self.btn_tour.deselect() # ceci relache le bouton radio

class Modele():
    def __init__(self,parent):
        self.parent=parent

class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.root.mainloop()

if __name__=="__main__":
    c=Controleur()