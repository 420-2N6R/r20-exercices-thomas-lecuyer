from datetime import datetime

class CompteBancaire :
    def __init__(self, compte_holder, balance=0) :
            listetransactions=[]
            self. compte_holder = compte_holder
            self.balance = balance
            self.liste_transactions=listetransactions    

    def deposer(self,montant):
            self.balance+=montant
            print(f"un depot de {montant} a été éffectué")
            print(f"le nouveau solde est de {self.balance}")
            new_transaction=f"{CompteBancaire.__temps_maintenant} dépot de {montant}$"
            self.liste_transactions.append(new_transaction)
    
    def retirer(self,montant):
            if montant < self.balance:
                  self.balance-=montant
                  new_transaction=f"{CompteBancaire.__temps_maintenant} retrait de {montant}$"
                  self.liste_transactions.append(new_transaction)
            else:
                  print("fonds insuffisants")  
            print(f"un retrait de {montant} a été éffectué")
            print(f"le nouveau solde est de {self.balance}")
    @staticmethod
    def aubaine():
           print("Épargner 50$ par mois vous donnera un montant de plus de 20 000$ dans 20 ans! ")

    @staticmethod
    def __temps_maintenant():
          return datetime.now().strftime("%H:%M:%S")

