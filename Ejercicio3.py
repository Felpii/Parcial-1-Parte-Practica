class Fruta:

    def __init__(self,color,sabor):
        self.color= color
        self.sabor= sabor

mango = Fruta("Amarrillo","Dulce")
uva = Fruta("Morada","Dulce")

print(type(mango))
print(type(uva))

print(mango.color,mango.sabor)
print(uva.color,uva.sabor)
       

