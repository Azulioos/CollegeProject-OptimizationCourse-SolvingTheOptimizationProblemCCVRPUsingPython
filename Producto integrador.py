from tkinter import *
from collections import deque
from math import sqrt
import numpy as np

f = open("VRPNC1m.txt", "r")
lines_clients = [line for line in f.readlines() if line[0:10]=="nbClients:"]
f.seek(0)
lines_trips = [line for line in f.readlines() if line[0:8]=="nbTrips:"]
f.seek(0)
veh_capacity = [line for line in f.readlines() if line[0:11]=="VehCapacity"]
f.seek(0)

Activador = 0
for line in f.readlines():

	if Activador == 1:
		clients_demands = []
		clients_demands = list(line.split())
		clientDemands = [int(x) for x in clients_demands]

		#print("Demanda de los clientes: ",  clientDemands)
		Activador = 0
	
	if line[0:14]=="ClientDemands:":
		Activador = 1


f.seek(0)


for line in f.readlines():

	if Activador == 1:
		services_times = []
		services_times = list(line.split())		
		serviceTimes = [int(x) for x in services_times]

		#print("Tiempos de servicio: ", serviceTimes)
		Activador = 0
	

	if line[0:13]=="ServiceTimes:":
		Activador = 1


f.seek(0)

#print("Coordenadas de los clientes: ")
coordinates = []
for line in f.readlines():

	if Activador == 1:
		coordinates.append(list(map(int, line.split())))

	if line[0:11]=="CoorX	CoorY":
		Activador = 1


#print(coordinates)
f.seek(0)

nbClients = int(lines_clients[-1].split()[1])
print("Numero de clientes: ", nbClients)

nbTrips = int(lines_trips[-1].split()[1])
print("Numero de rutas disponibles", nbTrips)

vehCapacity = int(veh_capacity[-1].split()[1])
print("Capacidad de vehiculos: ", vehCapacity)

matrizDeDistanciasX = []
matrizDeDistanciasY = []


x_ = 0
y_ = 0
for x in coordinates:

	for y in coordinates:

		if y == x:
			matrizDeDistanciasX.append(99999)

		else:
			Distancia = (sqrt(pow((coordinates[x_][0] - coordinates[y_][0]),2) + pow((coordinates[x_][1] - coordinates[y_][1]),2)))
			matrizDeDistanciasX.append(Distancia)

		y_ = y_ + 1

	matrizDeDistanciasY.append(list(matrizDeDistanciasX))

	x_ = x_ + 1
	y_ = 0
	matrizDeDistanciasX.clear()
    

Clients=nbClients+1
visitado=serviceTimes
sumlattot=0
while nbTrips>0:
    paso=1
    ultimo=0
    sumalatencia=0
    sumacapacidad=0
    ultimocliente=0
    print("0")
    while paso==1:
        paso=0
        menor=5000
        i=1
        while i<Clients:
            pes=sumacapacidad+clientDemands[i-1]
            if matrizDeDistanciasY[ultimocliente][i]<menor and pes<=vehCapacity and visitado[i-1]==0:
                posicion=i
                paso=1
                menor=matrizDeDistanciasY[ultimocliente][i]
            i=i+1
        if paso==1:
            sumalatencia=sumalatencia+matrizDeDistanciasY[ultimocliente][posicion]+ultimo
            ultimo=ultimo+matrizDeDistanciasY[ultimocliente][posicion]
            print("-",posicion)
            sumacapacidad=sumacapacidad+clientDemands[posicion-1]
            visitado[posicion-1]=1
            ultimocliente=posicion
        else:
            print("-0")
    print("La latencia es ", sumalatencia)
    sumlattot=sumlattot+sumalatencia
    nbTrips=nbTrips-1

print("La latencia total es ", sumlattot)