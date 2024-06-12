import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorContaminacion import generarContaminacionRios
from helpers.generarTabla import crearTablaHTML


#Para analizar datos con python debemos construir un dataframe

def construirDataFrameContaminacionRios():
    #Traigo los datos generados en el Mock
    datosContaminacionRios=generarContaminacionRios()

    #construyo el dataframe
    contaminacionRiosDF=pd.DataFrame(datosContaminacionRios,columns=['Comuna/Corregimiento','Cant Quebradas Contaminadas','Cant Quebradas Comuna/corregimiento'])

    #print(contaminacionRiosDF)
    #crearTablaHTML(contaminacionRiosDF,"contaminacionRios")

     #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    #print(contaminacionRiosDF)
    #contaminacionRiosDF.replace('-',pd.NA,inplace=True) 
    #contaminacionRiosDF.replace('sin',pd.NA,inplace=True) 

    #2. Limpiando (eliminando valores)
    #contaminacionRiosDF.replace('sin',pd.NA,inplace=True) 
    #contaminacionRiosDF.dropna(inplace=True)

  
    #AGRUPANDO DATOS
    datosAgrupados=contaminacionRiosDF.groupby("Comuna/Corregimiento")["Cant Quebradas Contaminadas"].mean()
    
    #GRAFICANDO DATOS
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='purple')
    plt.title('Cantidad de quebradas contaminadas por comuna/corregimiento')
    plt.xlabel('Comuna/Corregimiento')
    plt.ylabel('Cant Quebradas Contaminadas')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig("./assets/img/quebradas.png",format='png',dpi=300)
    #plt.show()

construirDataFrameContaminacionRios()