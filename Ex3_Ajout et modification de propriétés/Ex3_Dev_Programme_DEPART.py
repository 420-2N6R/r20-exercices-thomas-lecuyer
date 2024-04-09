import datetime

class Employe:
    def __init__(self,id_employe, prenom, nom, role, salaire):
        self.id_employe = id_employe
        self.prenom = prenom
        self.nom = nom
        self.role = role
        self.salaire = salaire
        self.courriel = prenom + '.' + nom +'@gmail.com'
        
    def __str__(self):
        info = f'\t ID: {self.id_employe}, \n\t Nom: {self.nom}, \n\t Prénom: {self.prenom}, \n\t Role: {self.role}'
        return info

class Programmeur(Employe): 
    def __init__(self,id_employe,prenom, nom, role, salaire,liste_fonctions=None):
        super().__init__(id_employe,prenom, nom, role, salaire)
        if (liste_fonctions != None):
            self.liste_fonctions = liste_fonctions
        else:
            self.liste_fonctions = []
    
    def coder(self,fonction):
        self.liste_fonctions.append(fonction)
        
    def __str__(self):
        info = super().__str__()
        info += f' \n\tListe de fonctions complétées: {self.liste_fonctions}'
        return info

class Designer(Employe): 
    def __init__(self,id_employe,prenom, nom, role, salaire,liste_artefacts=None):
        super().__init__(id_employe,prenom, nom, role, salaire)
        if (liste_artefacts != None):
            self.liste_artefacts = liste_artefacts
        else:
            self.liste_artefacts = []
    
    def dessiner(self,artefact):
        self.liste_artefacts.append(artefact)
        
    def __str__(self):
        info = super().__str__()
        info += f' \n\tListe de artéfacts complétés: {self.liste_artefacts}'
        return info

class Tech_Reseau(Employe): 
    def __init__(self,id_employe, prenom, nom, role, salaire,liste_interventions=None):
        super().__init__(id_employe, prenom, nom, role, salaire)
        if (liste_interventions != None):
            self.liste_interventions = liste_interventions
        else:
            self.liste_interventions = []
    
    def intervenir(self,intervention):
        self.liste_interventions.append(intervention)
        
    def __str__(self):
        info = super().__str__()
        info += f' \n\tListe des interventions complétées: {self.liste_interventions}'
        return info

class Equipe:
    def __init__(self,nom, liste_employes=None) -> None:
        self.nom = nom
        if (liste_employes != None):
            self.liste_employes = liste_employes
        else:
            self.liste_employes = []
        
    def ajouter_employe(self, cet_employe: Employe, date_debut, date_fin=None):
        info_employe = {'employe':cet_employe, 'date_debut':date_debut, 'date_fin': date_fin}
        if (info_employe not in self.liste_employes):
            self.liste_employes.append(info_employe)
            
    def enlever_employe(self, cet_employe: Employe):
        for donnee in self.liste_employes:
            if donnee["employe"] == cet_employe:
                donnee["date_fin"]= datetime.date.today()
                
    def imprimer_employes(self):
        for donnee in self.liste_employes:
            employe = donnee['employe']
            print(f"\t Employe: {employe.nom}, {employe.prenom} - Date début: {donnee['date_debut']} - Date fin: {donnee['date_fin']}")
                 
    def __str__(self) -> str:
        nb = 0
        for employe in self.liste_employes:
            if employe["date_fin"] == None:
                nb +=1
        info = f'\t Nom: {self.nom}, \n\t Nb Employes: {nb}'
        return info    

class Logiciel:
    def __init__(self,nom, etat, liste_equipes=None) -> None:
        self.nom = nom
        self.etat = etat
        if (liste_equipes != None):
            self.liste_equipes = liste_equipes
        else:
            self.liste_equipes = []
        
    def ajouter_equipe(self, cet_equipe: Equipe):
        if cet_equipe not in self.liste_equipes:
            self.liste_equipes.append(cet_equipe)
        
    def __str__(self) -> str:
        info = f'\t Nom: {self.nom}, \n\t Etat: {self.etat}, \n\t Nb Equipes: {len(self.liste_equipes)}'
        return info
 
# Instanciation d'un nouveau logiciel 
nouveau_logiciel = Logiciel("ZenithSuit", "Developpement")
print("\nInfos sur le nouveau logiciel, avec 0 équipe")
print(nouveau_logiciel)

# Instanciation d'une équipe de developpement pour ce nouveau logiciel
nouvelle_equipe = Equipe("Developpement")
print("\nInfos sur la nouvelle équipe")
print(nouvelle_equipe)
nouveau_logiciel.ajouter_equipe(nouvelle_equipe)
print("\nOn devrait voir que le nouveau logiciel a maintenant 1 équipe")
print(nouveau_logiciel)

# Instanciation d'un Programmeur qui sera le gestionnaire de l'équipe de développement
gestionnaire = Programmeur(1001,"Marc","Dupré","gestionnaire", 120000)
# Instanciation d'un Designer qui travaillera dès le départ dans l'équipe
top_designer = Designer(1002, "Amy", "Fortier", "top_designer", 95000)
# Instanciation d'un Tech_Reseau qui sera l'architecte principal de la solution
architecte_principal = Tech_Reseau(1003,"Luc", "Michaud", "architecte_principal", 150000)

# Ajout de ces trois employes dans la nouvelle équipe de developpement
nouvelle_equipe.ajouter_employe(gestionnaire, datetime.date.today())
nouvelle_equipe.ajouter_employe(top_designer,datetime.date.today())
nouvelle_equipe.ajouter_employe(architecte_principal,datetime.date.today())

# Ajout d'une fonction pour le gestionnaire
gestionnaire.coder("Entrevues pour remplir l'équipe")
print("\nInfos sur le gestionnaire:")
print(gestionnaire)
print("\nInfos sur le designer")
top_designer.dessiner("logo")
print(top_designer)
# Ajout de 2 interventions pour l'architecte principal
architecte_principal.intervenir("Mise en place de 3 serveurs")
architecte_principal.intervenir("Installation du vlan pour l'équipe de développement")
print("\nInfos sur l'architecte principal")
print(architecte_principal)

print("\nInfos sur la nouvelle equipe")
print(nouvelle_equipe)
nouvelle_equipe.imprimer_employes()
    
# Enlever la top_designer de l'équipe de développement
nouvelle_equipe.enlever_employe(top_designer)
print("\nInfos sur la nouvelle equipe, après le départ de la top_designer de l'équipe de développement")
print(nouvelle_equipe)
nouvelle_equipe.imprimer_employes()
