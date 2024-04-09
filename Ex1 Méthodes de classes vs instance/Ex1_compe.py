from datetime import datetime

class CompteBancaire :
    def __init__(self, compte_holder, balance=0) :
            self. compte_holder = compte_holder
            self.balance = balance

    def deposer(self):
          pass
    
    def retirer(self):
          pass
    
    #def aubaine

    @staticmethod
    def __temps_maintenant():
          return datetime.now().strftime("%H:%M:%S")

