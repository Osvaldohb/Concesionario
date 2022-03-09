import main
import persona

def vent():
    print("Nos da mucho gusto saber que elegiste comprar con nosotros\n")
    print("A continuacion te pediremos tus datos personales y tu metodo de pago\n")
    print("Que tipo de vehiculo decidiste comprar?\n")
    print("1.-Carro/Sedan") 
    print("2.-Camioneta")
    print("3.-Limosina") 
    dec=int(input())

    if(dec==1):
        print("Ingresa el nombre del auto")
        nc=input()
        print("\n")
        for r in range(len(main.cCarrs)):
            if(nc==main.cCarrs[r].nombre):
                ce=main.cCarrs[r]
    elif(dec==2):
        print("Ingresa el nombre de la camioneta")
        nc1=input()
        print("\n")
        for e in range(len(main.cCam)):
            if(nc1==main.cCam[e].nombre):
                ce=main.cCam[e]
    elif(dec==3):
        print("Ingresa el nombre de la limosina")
        nc2=input()
        print("\n")
        for g in range(len(main.cLim)):
            if(nc2==main.cLim[g].nombre):
                ce=main.cLim[g]   

    print("Ahora tus datos personales\n")
    print("Ingresa tu nombre")
    persona.Cliente.setNombre(persona.Cliente,input())
    print("Apellido paterno")
    persona.Cliente.setApatern(persona.Cliente,input())
    print("Apellido materno")
    persona.Cliente.setAmatern(persona.Cliente,input())
    print("Numero de telefono")
    persona.Cliente.setnumT(persona.Cliente,input())
    print("Calle")
    persona.Cliente.setcalle(persona.Cliente,input())
    print("Estado")
    persona.Cliente.setEst(persona.Cliente,input())
    print ("Municipio")
    persona.Cliente.setMuni(persona.Cliente,input())
    print ("Numero de casa")
    persona.Cliente.setnum(persona.Cliente,input())
    print("Ingresa tu edad")
    persona.Cliente.setEdad(persona.Cliente,input())
    print("Elige tu metodo de pago")
    print("1.-Efectivo")
    print("2.-Tarjeta")
    print("3.-Transferencia")
    lel=int(input())
    if(lel==1):
        met="Efectivo"
    elif(lel==2):
        met="Tarjeta"
    elif(lel==3):
        met="Transferencia"
    print("\n")
    persona.Cliente.setCatego(persona.Cliente,"Cliente")

    cliente1=persona.Cliente()
    print("El cliente con la informacion:\n")
    print("Nombre: "+cliente1.getNombre())
    print("Apellido Parteno: "+cliente1.getApatern())
    print("Apellido Materno: "+cliente1.getAmatern())
    print("Nombre: "+cliente1.getnumT())
    print("Calle: "+cliente1.getcalle())
    print("Estado: "+cliente1.getEst())
    print("Municipio: "+cliente1.getMuni())
    print("Numero Casa: "+cliente1.getnum())
    print("Edad: "+cliente1.getEdad())
    print("Categoria: "+cliente1.getCatego())

    print("\n")
    print("Aqui esta la informacion de tu nuevo vehiculo")
    print(ce)
    print("\n")
    print("Aqui esta tu metodo de pago")
    print(met)
    print("\n")


    