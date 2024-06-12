import random

def generarBiodiversidad():
    listaDatos=[]
    for i in range(1000):
        corregimientoComuna=random.choice(['San Antonio de Prado','Santa Elena','Palmitas','San Cristobal','Altavista','comuna 1 popular','comuna 2 Sana Cruz','comuna 3 Manrique','comuna 4 Aranjuez','comuna 5 Castilla','comuna 6 12 de Octubre','comuna 7 Robledo','comuna  Villa Hermosa','comuna 9 Buenos Aires','comuna 10 La Candelaria','comuna 11 Laureles','comuna 12 La America','comuna 13 San Javier','comuna 14 el Poblado','comuna 15 Guayabal','comuna 16 Belen'])
        guardabosques=random.randint(0,10000)
        cantidadEspecies=random.randint(0,10000)
        especiesPredominante=random.choice(['Aves','Insectos','Roedores','Felinos'])
        biodiversidad=[corregimientoComuna,guardabosques,cantidadEspecies,especiesPredominante]

        listaDatos.append(biodiversidad)
 
    return listaDatos 
   
