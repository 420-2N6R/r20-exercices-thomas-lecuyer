#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    def calculer_paie(self, employes):
        print("Calcul de la paie des employes")
        print("==============================")
        for employe in employes:
            print(f'Paie de: {employe.id} - {employe.nom}')
            print(f' - montant net de:  {employe.calculer_paie()}')
            print('')
            
class Employe(ABC):
    
    liste_employes = []
    
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        Employe.liste_employes.append(self)
        
    @abstractmethod
    def calculer_paie():
        pass
    
class Employe_salarie(Employe):
    def __init__(self, id, nom, salaire_par_semaine):
        super().__init__(id, nom)
        self.salaire_par_semaine = salaire_par_semaine
        
    def calculer_paie(self):
        return self.salaire_par_semaine
 
class Employe_heure(Employe):  
    def __init__(self, id, nom, heures_travaillees, taux_horaire):
        super().__init__(id, nom)
        self.heures_travaillees = heures_travaillees
        self.taux_horaire = taux_horaire
        
    def calculer_paie(self):
        return self.heures_travaillees * self.taux_horaire
    
class Employe_commission(Employe_salarie):  
    def __init__(self, id, nom, salaire_par_semaine, commission):
        super().__init__(id, nom, salaire_par_semaine)
        self.commission = commission

        
    def calculer_paie(self):
        salaire_fixe = super().calculer_paie()
        return salaire_fixe + self.commission
        
employe_salarie1 = Employe_salarie(1, 'Marc Tremblay', 2100)
employe_heure1 = Employe_heure(2,'Pierre Jonhson', 40, 22)
employe_commission1 = Employe_commission(3, 'Luc Toupin', 1400, 600)
#employex = Employe(4,'Lucie Rangers')


systeme_de_paie_hr = Systeme_de_paie()
systeme_de_paie_hr.calculer_paie([employe_salarie1,employe_heure1,employe_commission1])


    
     