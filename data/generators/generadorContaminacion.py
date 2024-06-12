import random

def generarContaminacionRios():
    listaDatos=[]
    for i in range(1000):
        comunaCorregimiento=random.choice(['comuna 1 popular','comuna 2 Sana Cruz','comuna 3 Manrique','comuna 4 Aranjuez','comuna 5 Castilla','comuna 6 12 de Octubre','comuna 7 Robledo','comuna  Villa Hermosa','comuna 9 Buenos Aires','comuna 10 La Candelaria','comuna 11 Laureles','comuna 12 La America','comuna 13 San Javier','comuna 14 el Poblado','comuna 15 Guayabal','comuna 16 Belen','San Antonio de Prado','Santa Elena','Palmitas','San Cristobal','Altavista'])
        cantidadQuebradasContaminadas=random.randint(0,100)
        cantidadQuebradasComunaCorregimiento=random.randint(0,100)
        contaminacionRios=[comunaCorregimiento,cantidadQuebradasContaminadas,cantidadQuebradasComunaCorregimiento]

        listaDatos.append(contaminacionRios)
 
    return listaDatos 
   
