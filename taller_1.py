#Leonardo Perez
CanPers = int(input("¿Cuantas personas desea registrar?: "))
Regist = True
i = 0
while Regist:
    i = i + 1
    print(f"\nParticipante #{i}:")
    Nombre = input("Ingrese el nombre: ")
    Edad = int(input("Ingrese la edad: "))
    while Edad <= 0:
        print("ERROR: Ingrese la edad en un formato válido")
        Edad = int(input("Ingrese la edad: "))
    Conbas = input("¿Tiene conocimientos Básicos de computación?: s = si, n = no:  ")
    if Edad >= 15 and Conbas.lower() == "s" :
            print("\n-----------Puede participar en el taller-----------\n")
    elif Edad < 15 or Conbas.lower() == "n": 
            print("\n-----------No cumple los requisitos-----------\n")   
    if i == CanPers:
        Regist = False
        print("-----------   Proceso finalizado   -----------")
    

print("holaaaaaaaaaaaaaaaaaaaaaa mundoooooo")
    