import random

def generarSiembraArboles():
    listaDatos=[]
    for i in range(1000):
        corregimiento=random.choice(['San Antonio de Prado','Santa Elena','Palmitas','San Cristobal','Altavista'])
        id=random.randint(0,1000000)
        nombreEncuestado=random.choice(['Pedro Paramo','Sandra Mor','Martina la Peligrosa','Kevin Albeiro','Valentina Mor','Juan Jimeno'])
        hectareasUltimoAno=random.randint(0,10000)
        especiesSembradas=random.choice(['Almendros','Álamo','Palma de cera','Guayacanes','Pinos','Olivos'])
        siembraArboles=[corregimiento,id,nombreEncuestado,hectareasUltimoAno,especiesSembradas]

        listaDatos.append(siembraArboles)
 
    return listaDatos 
   
