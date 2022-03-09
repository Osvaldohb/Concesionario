import persona

def creden(usuario,passw):
 if(usuario=="Admin" and passw=="Admin"):
    print("Bienvenido al menu de administrador")
    print("Aqui podras cambiar algunos parametros de los empleados")
    print("1.-Cambiar edad")
    print("2.-Cambiar numero de telefono")
    dec=int(input())
    if(dec==1):
        persona.cambiarEdad()
    elif(dec==2):
        persona.cambiarTelefono()