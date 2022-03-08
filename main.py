from random import randint
from typing import overload
from tqdm import tqdm

class Automovil:
    def __init__(self,tipo,color, marca, modelo, nombre, motor, tcomb, kilome,estado, costo):
        self.tipo=tipo
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.nombre=nombre
        self.motor=motor
        self.tcomb=tcomb
        self.kilome=kilome
        self.estado=estado
        self.costo=costo

    def __str__(self):
        return(f"Tipo:{self.tipo}\n"+f"Color:{self.color}\n"+f"Marca:{self.marca}\n"+f"Modelo:{self.modelo}\n"+f"Nombre:{self.nombre}\n"+f"Motor:{self.motor}\n"+f"Combustible:{self.tcomb}\n"+f"Kilometraje:{self.kilome}\n"+f"Estado:{self.estado}\n"+f"Costo: {self.costo}\n")

    def getTipo(self):
        return self.tipo
    def getColor(self):
        return self.color
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getNombre(self):
        return self.nombre
    def getMotor(self):
        return self.motor
    def getTcomb(self):
        return self.tcomb
    def getKilom(self):
        return self.kilome
    def getEstado(self):
        return self.estado

    def setTipo(self, x):
        self.tipo=x
    def setColor(self, x):
        self.color=x
    def setMarca(self, x):
        self.marca=x
    def setModelo(self,x):
        self.modelo=x
    def setNombre(self, x):
        self.nombre=x
    def setMotor(self, x):
        self.motor=x
    def setTcomb(self, x):
        self.tcomb=x
    def setKilom(self,x):
        self.kilome=x
    def setEstado(self, x):
        self.estado=x

    def arranque(self):
        print("Estoy arrancando")

    def color(self):
       print(self.getColor())

    def IniciarPrueba(self):
        print("Se esta iniciando la prueba de manejo\n")
        loop=tqdm(total=40000,position=0,leave=False)
        for k in range(40000):
            loop.set_description("Manejando...".format(k))
            loop.update(1)
        print("\n")    
        print("La prueba de manejo se a terminado con exito! \n")

class Carro(Automovil):
  pass
car1=Carro('Carro','Guinda','Chevrolet',2000,'Cavalier',2.2, 'Gasolina',2000,"Usado",35000)
car2=Carro('Carro','Rojo','Audi',2022,'A3 Sedan',2.0, 'Gasolina',0,"Nuevo",609900)
car3=Carro('Carro','Azul','Ford',2006,'Fiesta',1.6, 'Gasolina',180000,"Usado",45000)
car4=Carro('Carro','Blanco','Chevrolet',2012,'Aveo',1.6, 'Gasolina',74016,"Semi-Nuevo",120000)
car5=Carro('Carro','Gris','Tesla',2017,'Model S',175, 'Electrico',22701,"Semi-Nuevo",1120000)


class Camioneta(Automovil):
  pass
cam1=Camioneta('Camioneta','Blanca','Chevrolet',2020,'Silverado',5.3, 'Gasolina',0,"Nuevo",100000)
cam2=Camioneta('Camioneta','Roja','GMC',2019,'Terrain',1.5, 'Gasolina',30000,"Seminuevo",679000)
cam3=Camioneta('Camioneta','Azul','RAM',2019,'Heavy Duty',3.6, 'Disel',100,"Seminuevo",350000)
cam4=Camioneta('Camioneta','Amarilla','Jeep',2018,'Silverado',5.3, 'Gasolina',0,"Nuevo",100000)
cam5=Camioneta('Camioneta','Amarilla','Toyota',2010,'Silverado',5.3, 'Gasolina',0,"Nuevo",100000)

class Limosina(Automovil):
  pass
car21=Limosina('Carro','Guinda','Chevrolet',2000,'Cavalier',2.2, 'Gasolina',2000,"Usado",35000)

cCarrs=[car1,car2,car3,car4,car5]
cCam=[cam1,cam2,cam3,cam4,cam5]        
def mostrar():
    for x in range(len(cCarrs)):
        print(cCarrs[x])
        print(cCam[x]) 
                 
print("Bienvenido a Concesionaria de Autos 'Aguila Blanca'\n")
print("Este es nuestro menu\n")
print("1.-Venta de nuestros automoviles\n")
print("2.-Te mostramos nuestro catalogo\n")
print("3.-Busqueda \n")

n=int(input("\n Que desea realizar:"))

if(n==1):
    pass
elif(n==2):
    mostrar()
elif(n==3):
    pass



