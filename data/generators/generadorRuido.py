import random

def generarRuido():
    listaDatos=[]
    for i in range(1000):
        comuna=random.choice(['comuna 1 popular','comuna 2 Sana Cruz','comuna 3 Manrique','comuna 4 Aranjuez','comuna 5 Castilla','comuna 6 12 de Octubre','comuna 7 Robledo','comuna 8 Villa Hermosa','comuna 9 Buenos Aires','comuna 10 La Candelaria','comuna 11 Laureles','comuna 12 La America','comuna 13 San Javier','comuna 14 el Poblado','comuna 15 Guayabal','comuna 16 Belen'])
        totalPoblacion=random.choice(['3000','4500','5000','10000','7500','6000','6500','7000','3000','12000','13000','11500','10700','9500','10100','11000'])
        tamanoMuestra=random.choice(['2000','2500','3000','8000','4500','3000','2500','3500','1000','6000','7000','5500','4700','4500','6000','7000'])
        decibelesDia=random.randint(0,180)
        deciblesNoche=random.randint(0,180)
        fecha=random.choice(["2024-05-14","2024-05-15"])
        nombreEncuestado=random.choice(['Pedro Paramo','Sandra Mor','Martina la Peligrosa','Kevin Albeiro','Valentina Mor','Juan Jimeno'])
        id=random.randint(0,1000000)
        nombreEdificio=random.choice(['Almendros','Terranova','Sonatto','Entre Bosques','Fragua','Olivar'])
        ruido=[comuna,totalPoblacion,tamanoMuestra,decibelesDia,deciblesNoche,fecha,nombreEncuestado,id,nombreEdificio]

        listaDatos.append(ruido)
 
    return listaDatos 
   

