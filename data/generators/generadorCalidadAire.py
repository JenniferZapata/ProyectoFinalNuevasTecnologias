#Rutina para generar de forma aletoria multiples datos con python

import random

def generarDatosCalidadAire():
    listaDatos=[]
    for i in range(1000):
        comuna=random.choice(['comuna 1 popular','comuna 2 Sana Cruz','comuna 3 Manrique','comuna 4 Aranjuez','comuna 5 Castilla','comuna 6 12 de Octubre','comuna 7 Robledo','comuna 8 Villa Hermosa','comuna 9 Buenos Aires','comuna 10 La Candelaria','comuna 11 Laureles','comuna 12 La America','comuna 13 San Javier','comuna 14 el Poblado','comuna 15 Guayabal','comuna 16 Belen','sin','-'])
        totalPoblacion=random.choice(['3000','4500','5000','10000','7500','6000','6500','7000','3000','12000','13000','11500','10700','9500','10100','11000'])
        tamanoMuestra=random.choice(['2000','2500','3000','8000','4500','3000','2500','3500','1000','6000','7000','5500','4700','4500','6000','7000'])
        ica=random.randint(20,100)
        fecha=random.choice(["2024-05-14","2024-05-15"])
        nombreEncuestado=random.choice(['Pedro Paramo','Sandra Mor','Martina la Peligrosa','Kevin Albeiro','Valentina Mor','Juan Jimeno'])
        id=random.randint(0,1000000)
        calidadAire=[comuna,totalPoblacion,tamanoMuestra,ica,fecha,nombreEncuestado,id]

        listaDatos.append(calidadAire)
 
    return listaDatos 
   




