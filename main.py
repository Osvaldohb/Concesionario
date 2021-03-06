
from random import randint
from tqdm import tqdm
import venta 
import admin
import os

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

    def IniciarPrueba():
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
cam4=Camioneta('Camioneta','Morada','Jeep',2018,'4*4',5.3, 'Electrica',0,"Nueva",2000000)
cam5=Camioneta('Camioneta','Amarilla','Toyota',2010,'ROCK',5.3, 'Gasolina',0,"Nuevo",100000)

class Limosina(Automovil):
  pass
lim1=Limosina('Limosina','Amarilla','LINCOLN',2018,'LUMISINAS',2.8, 'Gasolina',0,"NUEVA",35000000)
lim2=Limosina('Limosina','Azul','MERCEDES',2019,'CLASE S',2.7, 'DISEL',100,"SEMINUEVA",25000000)
lim3=Limosina('Limosina','Negra','CHYSLER',2020,'WALTER',2.4, 'ELECTRICA',200,"SEMINUEVA",2000000)
lim4=Limosina('Limosina','Morada','HUMMER',2021,'RJRED',2.3, 'Gasolina',300,"SEMINUEVA",5000000)
lim5=Limosina('Limosina','Blanca','ROLLS ROYCE',2022,'ROYCE',2.2, 'ELECTRI',50,"SEMINUEVA",9999999)

cCarrs=[car1,car2,car3,car4,car5]
cCam=[cam1,cam2,cam3,cam4,cam5]   
cLim=[lim1,lim2,lim3,lim4,lim5]     
def mostrar():
    for x in range(len(cCarrs)):
        print(cCarrs[x])
        print(cCam[x]) 
        print(cLim[x])

def busqueda():
    print("Porfavor indicanos que estas buscando\n")
    print("1.-Carro/Sedan") 
    print("2.-Camioneta")
    print("3.-Limosina")   
    x=int(input())
    a=0
    if(x==1):
        print("Si tienes algun nombre por favor introducelo lo buscaremos en nuestro stock de lo contrario teclea No y te mostraremos todos los veiculos")
        nome=str(input())
        print("\n")
        for i in range(len(cCarrs)):
            if(nome==cCarrs[i].nombre):
                print(cCarrs[i])
                a=int(1)

        for y in range(len(cCarrs)):
            if(nome=="No"):
                print(cCarrs[y])
        if(a==0):
            print("Lo sentimos no encontramos tu busqueda")            
    elif(x==2):
        print("Si tienes algun nombre por favor introducelo lo buscaremos en nuestro stock de lo contrario teclea No y te mostraremos todas las Camionetas")
        nome=str(input())
        print("\n")
        for a in range(len(cCam)):
            if(nome==cCam[a].nombre):
                print(cCam[a])
                a=int(1)       
        for p in range(len(cCam)):
            if(nome=="No"):
                print(cCam[p])
        if(a==0):
            print("Lo sentimos no encontramos tu busqueda") 

    elif(x==3):
        print("Si tienes algun nombre por favor introducelo lo buscaremos en nuestro stock de lo contrario teclea No y te mostraremos todas las limosinas")
        nome=str(input())
        print("\n")
        for b in range(len(cLim)):
            if(nome==cLim[b].nombre):
                print(cLim[b])
                a=int(1)
        for c in range(len(cLim)):
            if(nome=="No"):
                print(cLim[c]) 
        if(a==0):
            print("Lo sentimos no encontramos tu busqueda") 
            
               
          
                
print("Bienvenido a Concesionaria de Autos 'Aguila Blanca'\n")
print("Este es nuestro menu")
print("1.-Venta de nuestros automoviles")
print("2.-Te mostramos nuestro catalogo")
print("3.-Busqueda ")
print("4.-Prueba de manejo")
print("5.-Administrador")

n=int(input("\n Que desea realizar:"))

if(n==1):
    os.system("cls")
    venta.vent()
elif(n==2):
    os.system("cls")
    mostrar()
elif(n==3):
    os.system("cls")
    busqueda()
elif(n==4):
    os.system("cls")
    print("Ingresa el coche a probar")
    nome1=input()
    print("Se inicia la prueba en el veiculo..."+nome1)
    Automovil.IniciarPrueba()    
elif(n==5):
    os.system("cls")
    print("ADVERTENCIA ESTE MENU ES SOLO PARA EL ADMINISTRADOR")
    print("Ingresa el usuario")
    usu=input()
    print("Ingresa la contrase??a")
    contra=input()
    admin.creden(usu,contra)




