#Una empresa llamada "Transportes Cesde" requiere guardar los nombres de los conductores
# y el dinero que recaudan cada dia de la semana. desde el lunes hasta el sabado
#movilizando a la comunidad educativa y el porcentaje de recaudo de cada conductor.
#para guardar esta informacion use las iguientes listas:
#NombreConductor, DiasSemana, Recaudo y generar una lista llamada totalRecaudo con la suma total de lo 
#recaudado por cada conductor.
#Debe solicitar el numero de conductores qye hacen parte de la empresa.

NombreConductor = []
DiasSemana = []
Recaudo = []
totalRecaudo = []
#Solicitar el numero de conductores
numConductores = int(input("Ingrese el numero de conductores: "))
#Solicitar los datos de cada conductor
for i in range(numConductores):
    NombreConductor.append(input("Ingrese el nombre del conductor: "))
    DiasSemana.append(input("Ingrese el dia de la semana: "))
    Recaudo.append(int(input("Ingrese el recaudo: ")))
    totalRecaudo.append(Recaudo[i])
    print()
#Mostrar los datos de cada conductor
for i in range(numConductores):
    print("Conductor: ", NombreConductor[i])
    print("Dia: ", DiasSemana[i])
    print("Recaudo: ", Recaudo[i])
    print()
#Mostrar el total de recaudo de cada conductor
for i in range(numConductores):
    print("Total recaudado por el conductor ", NombreConductor[i], " es: ", totalRecaudo[i])
    print()
#Mostrar el total de recaudo de todos los conductores
print("Total recaudado por todos los conductores: ", sum(totalRecaudo))
print()
#Mostrar el porcentaje de recaudo de cada conductor
for i in range(numConductores):
    print("Porcentaje de recaudo del conductor ", NombreConductor[i], " es: ", (totalRecaudo[i]/sum(totalRecaudo))*100)
    print()
#Mostrar el porcentaje de recaudo de todos los conductores
for i in range(numConductores):
    print("Porcentaje de recaudo del conductor ", NombreConductor[i], " es: ", (totalRecaudo[i]/sum(totalRecaudo))*100)
    
