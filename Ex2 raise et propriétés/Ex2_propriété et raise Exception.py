from math import pi
#1. Ajouter un raise Exception qui lèvera une exception de type TypeError si le type de paramètre passé
#        lors du __init__ n’est pas un int ou float ( vous pouvez utiliser la fonction type() )

#2.	Ajouter un raise Exception qui lèvera une exception de type ValueError  si la valeur du rayon est 
#       égale ou inférieure à 0

#3.	Terminer la propriété rayon

#4.	Ajouter un setter à la propriété rayon. Le setter doit faire les mêmes vérifications que dans 
#       le __init__ afin de s’assurer que le rayon est correct.

#5.	Terminer les propriétés, circonférence, volume et aire qui ont déjà été déclarés dans la classe.
#       (NOTEZ : la valeur de pi à été importer, vous pouvez utilisé pi comme une constante)




class Sphere:
    def __init__(self, pRayon) -> None:
        if type(pRayon) != int and type(pRayon) != float:
            raise TypeError("mauvais type de donnée")
        elif pRayon<=0:
            raise ValueError("la valeur n'est pas valide")
        else: self._rayon = pRayon
    
    @property
    def rayon(self) :
        return self._rayon

    @property
    def circonference(self):
        return 2*self._rayon*pi # la circonférence d'une sphère est égal à " 2 * pi * rayon "

    @property
    def volume(self):
        return (4/3)*pi*(self._rayon**3) # le volume d'une sphère est égale à " 4/3 * pi * (rayon ** 3) "

    @property
    def aire(self):
        return pi*self._rayon**2


if __name__ == "__main__" :
    print(pi) #voyez que vous pouvez utilisé la constante pi

    #Testez votre code, voir l'énoncé

new_cercle=Sphere(20)

print(new_cercle.circonference)
print(new_cercle.volume)
print(new_cercle.aire)