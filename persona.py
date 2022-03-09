import main
class Persona:
    
    def __str__(self):
        return(f"Nombre:{self.nombre}\n"+f"Apellido Paterno:{self.ap}\n"+f"Apellido Materno:{self.am}\n"+f"Telefono:{self.numT}\n"+f"Estado:{self.est}\n"+f"Municipio:{self.mun}\n"+f"Calle:{self.calle}\n"+f"No. Casa:{self.num}\n"+f"Categoria:{self.catego}\n"+f"Edad: {self.edad}\n")

    def getNombre(self):
        return self.nombreP
    def getApatern(self):
        return self.ap
    def getAmatern(self):
        return self.am
    def getnumT(self):
        return self.numT
    def getcalle(self):
        return self.calle
    def getEst(self):
        return self.est
    def getnum(self):
        return self.num
    def getCatego(self):
        return self.catego
    def getEdad(self):
        return self.edad
    def getMuni(self):
        return self.mun

  
    def setNombre(self,x):
        self.nombreP=x
    def setApatern(self,x):
        self.ap=x
    def setAmatern(self,x):
        self.am=x
    def setnumT(self,x):
        self.numT=x
    def setcalle(self,x):
        self.calle=x
    def setEst(self,x):
        self.est=x
    def setnum(self,x):
        self.num=x
    def setCatego(self,x):
        self.catego=x
    def setEdad(self, x):
        self.edad=x
    def setMuni(self,x):
        self.mun=x


    def updateAge(self):
        print("A que edad es a la cual deseas actualizar?")
        self.edad=input()
        print("Esta es tu nueva edad: ",self.edad)

class Cliente(Persona):
    pass 
class Vendedor(Persona):
    pass

vend1=Vendedor()
vend1.setNombre("Osvaldo")
vend1.setApatern("Santillan")
vend1.setAmatern("Jimenez")
vend1.setnumT(7715696746)
vend1.setcalle("Aldama")
vend1.setEst("Hidalgo")
vend1.setnum(35)
vend1.setCatego("Vendedores")
vend1.setEdad(19)
vend1.setMuni("Apan")


vend2=Vendedor()
vend2.setNombre("Alexis")
vend2.setAmatern("Lozano")
vend2.setApatern("Franco")
vend2.setnumT(7751655383)
vend2.setcalle("Independencia")
vend2.setEst("Hidalgo")
vend2.setnum(0)
vend2.setCatego("Vendedor")
vend2.setEdad(18)
vend2.setMuni("Tepeapulco")

vend3=Vendedor()
vend3.setNombre("Elias")
vend3.setAmatern("Trejo")
vend3.setApatern("Rodriguez")
vend3.setnumT(7751655381)
vend3.setcalle("Revolucion")
vend3.setEst("Queretaro")
vend3.setnum(24)
vend3.setCatego("Vendedor")
vend3.setEdad(18)
vend3.setMuni("Peñitas")