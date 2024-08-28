class Vehiculo:

    def __init__(self,color,modelo):
        self.color= color
        self.modelo= modelo

carro = Vehiculo("Amarrillo","Toyota")
moto = Vehiculo("Negro","Mt09vs3")

print(type(carro))
print(type(moto))

print(carro.color,carro.modelo)
print(moto.color,moto.modelo)
       



