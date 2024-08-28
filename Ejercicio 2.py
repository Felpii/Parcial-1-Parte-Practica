class Mascota:

    def __init__(self,color,raza):
        self.color= color
        self.raza= raza

perro = Mascota("Blanco","Lobo siberiano")
gato = Mascota("Negro","Siames")

print(type(perro))
print(type(gato))

print(perro.color,perro.raza)
print(gato.color,gato.raza)
       

