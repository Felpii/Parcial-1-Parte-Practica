class Mascota:

    def __init__(self,color,raza):
        self.color= color
        self.raza= raza

perro = Mascota("Amarrillo","Shiba-inu")
gato = Mascota("Piel","Dwelf")

print(type(perro))
print(type(gato))

print(perro.color,perro.raza)
print(gato.color,gato.raza)
       



