import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorRuido import generarRuido
from helpers.generarTabla import crearTablaHTML

#Para analizar datos con python debemos construir un dataframe

def construirDataFrameRuido():
    #Traigo los datos generados en el Mock
    datosRuido=generarRuido()

    #construyo el dataframe
    ruidoDF=pd.DataFrame(datosRuido,columns=['Comuna','Total Poblacion','Tamaño Muestra','Decibeles Dia','Decibeles Noche','Fecha','Nombre','ID','Nombre Edificio'])

     #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    #print(ruidoDF)
    #ruidoDF.replace('-',pd.NA,inplace=True) 
    #ruidoDF.replace('sin',pd.NA,inplace=True) 

    #2. Limpiando (eliminando valores)
    #ruidoDF.replace('sin',pd.NA,inplace=True) 
    #ruidoDF.dropna(inplace=True)

    #3. Filtrando datos para depurar la información
    #Filtrar datos es obtener nuevos dataframes al aplicar condiciones logicas, también puede ser contar datos o consultar datos especificos
    #filtroDecibelesDia=ruidoDF.query("(decibelesDia>=20) and (decibelesDia<50)")
    #filtroDecibelesNoche=ruidoDF.query("(decibelesDia>=50) and (decibelesDia<70)")
    #filtroDecibelesDia=ruidoDF.query("(decibelesDia>=70)").value_counts()

    #AGRUPANDO DATOS
    datosAgrupadosD=ruidoDF.groupby("Comuna")["Decibeles Dia"].mean()
    datosAgrupadosN=ruidoDF.groupby("Comuna")["Decibeles Noche"].mean()
    
    #GRAFICANDO DATOS
    # plt.figure(figsize=(20,20))
    # datosAgrupadosD.plot(kind='bar',color='green')
    # plt.title('Decibeles por comuna día')
    # plt.xlabel('Comuna')
    # plt.ylabel('Decibeles Dia')
    # plt.grid(True)
    # plt.xticks(rotation=45)
    # plt.savefig("./assets/img/decibelesDia.png",format='png',dpi=300)
    #plt.show()
    
    plt.figure(figsize=(20,20))
    datosAgrupadosN.plot(kind='bar',color='blue')
    plt.title('Decibeles por comuna noche')
    plt.xlabel('Comuna')
    plt.ylabel('Decibeles Noche')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig("./assets/img/decibelesNoche.png",format='png',dpi=300)

    #print(ruidoDF)
    #crearTablaHTML(ruidoDF,"ruido")

    

    

    

construirDataFrameRuido()