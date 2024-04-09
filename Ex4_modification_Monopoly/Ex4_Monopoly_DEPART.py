
# Maintenant que nous sommes plus expérimentés, 
# nous allons mieux encapsuler les attributs de nos classes.

#Voyez l'énoncé pour voir ce que vous devez faire

class Terrain:
    def __init__(self,nom,couleur,est_a_vendre,prix) -> None:
        self._nom = nom
        self._couleur = couleur
        self._prix = prix

    @property
    def nom(self):
        return self._nom
    @property
    def couleur(self):
        return self._couleur
    @property
    def prix(self):
        return self._prix

    @nom.setter
    def nom(self):
        print("impossible de changer le nom")
    @couleur.setter
    def couleur(self):
        print("impossible de changer la couleur")
    @prix.setter
    def prix(self,new_prix):
        if new_prix > self._prix:
            self._prix=new_prix
        else:
            raise ValueError("le nouveau prix doit etre superieur a l'ancien")

    def __str__(self) -> str:
        return self.nom

class Banque:
    def __init__(self,montant_cash,list_terrains:list) -> None:
        self._montant_cash = montant_cash
        self.list_terrains = list_terrains
        self._montant_parc_immobilier=0
    
    @property
    def montant_cash(self):
        return self._montant_cash

    @montant_cash.setter
    def montant_cash(self,new_montant):
        try:
            if type(new_montant) ==float:
                self._montant_cash=new_montant
        except:
            print("mauvais type de donnée")
    
    def valeur_immo(self):
        valeur=0
        for terrain in self.list_terrains:
            valeur+=terrain.prix
        return(f"le parx immobilie vaut presentement {valeur}")
class Joueur:
    def __init__(self,montant_cash,list_terrains) -> None:
        self._montant_cash = montant_cash
        self.list_terrains = list_terrains

    @property
    def montant_cash(self):
        return self._montant_cash

    @montant_cash.setter
    def montant_cash(self, new_montant):
        if type(new_montant)==float:
            self._montant_cash=new_montant
        else:
            raise TypeError("mauvais type")
    def acheter(self,proprietaire,terrain:Terrain): 
        if self.montant_cash >= terrain.prix:
            if (terrain in proprietaire.list_terrains):
                proprietaire.list_terrains.remove(terrain)
                self.list_terrains.append(terrain)
                proprietaire.montant_cash += terrain.prix
                self.montant_cash -= terrain.prix
            else:
                print("Désolé, je n'ai pas ce terrain à vendre")
        else:
            print("Vous n'avez pas suffisament d'argent.")
       
            
#-	‘Avenue Kentucky’, rouge, 220000
#-	‘Avenue Pennsylvanie’, vert, 320000
#-	‘Promenade’, bleu, 400000
#Instanciez la banque, avec 22 millions de cash, et la liste de ces 3 terrains
#Instanciez un joueur qui a 1 million et une liste vide de terrains.
kentucky = Terrain('Avenue Kentucky','rouge',True,220000)
pennsylvanie = Terrain('Avenue Pensylvanie','vert',True,320000)
promenade = Terrain('Promenade','bleu',True,400000)

banque = Banque(22000000,[kentucky,pennsylvanie,promenade])
print(banque.valeur_immo())

joueur1 = Joueur(1000000,[])
joueur2 = Joueur(1000000,[])


print("joueur1 essaie d'acheter à la banque le terrain promenade")
joueur1.acheter(banque,promenade)

print('infos du joueur 1')
print(joueur1.montant_cash)
for terrain in joueur1.list_terrains:
    print(terrain)
#print(joueur1.list_terrains)

print('infos de la banque')
print(banque.montant_cash)
for terrain in banque.list_terrains:
    print(terrain)
#print(banque.list_terrains)


print("joueur2 essaie d'acheter au joueur1 le terrain promenade")
joueur2.acheter(joueur1,promenade)
print('infos du joueur 2')
print(joueur2.montant_cash)
for terrain in joueur2.list_terrains:
    print(terrain)
    
print('infos du joueur 1')
print(joueur1.montant_cash)
for terrain in joueur1.list_terrains:
    print(terrain)
    
print('infos de la banque')
print(banque.montant_cash)
for terrain in banque.list_terrains:
    print(terrain)    

print("joueur2 essaie d'acheter au joueur1 un terrain que le joueur1 n'a pas")
# joueur2 essaie d'acheter au joueur1 un terrain que le joueur1 n'a pas
joueur2.acheter(joueur1,kentucky)
print('infos du joueur 1')
print(joueur1.montant_cash)
for terrain in joueur1.list_terrains:
    print(terrain)
    
print('infos du joueur 2')
print(joueur2.montant_cash)
for terrain in joueur2.list_terrains:
    print(terrain)
    
print('infos de la banque')
print(banque.montant_cash)
for terrain in banque.list_terrains:
    print(terrain)   