import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorSiembraArboles import generarSiembraArboles
from helpers.generarTabla import crearTablaHTML

#Para analizar datos con python debemos construir un dataframe

def construirDataFrameSiembraArboles():
    #Traigo los datos generados en el Mock
    datosSiembraArboles=generarSiembraArboles()

    #construyo el dataframe
    siembraArbolesDF=pd.DataFrame(datosSiembraArboles,columns=['Corregimiento','ID','Nombre','Hectareas Ultimo Año','Especies Sembradas'])

     #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    #print(siembraArbolesDF)
    #siembraArbolesDF.replace('-',pd.NA,inplace=True) 
    #siembraArbolesDF.replace('sin',pd.NA,inplace=True) 

    #2. Limpiando (eliminando valores)
    #siembraArbolesDF.replace('sin',pd.NA,inplace=True) 
    #siembraArbolesDF.dropna(inplace=True)

    #3. Filtrando datos para depurar la información
    #Filtrar datos es obtener nuevos dataframes al aplicar condiciones logicas, también puede ser contar datos o consultar datos especificos
    #filtrohectareasUltimoAnoBajo=siembraArbolesDF.query("(hectareasUltimoAno>=1) and (hectareasUltimoAno<1000)")
    #filtrohectareasUltimoAnoMedio=siembraArbolesDF.query("(hectareasUltimoAno>=1000) and (hectareasUltimoAno<5000)")
    #hectareasUltimoAnoAlto=siembraArbolesDF.query("(hectareasUltimoAno>=5000)").value_counts()


    #AGRUPANDO DATOS
    datosAgrupados=siembraArbolesDF.groupby("Corregimiento")["Hectareas Ultimo Año"].mean()
    
    #GRAFICANDO DATOS
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='red')
    plt.title('Hectareas sembradas al año por corregimiento')
    plt.xlabel('Corregimiento')
    plt.ylabel('Hectareas Ultimo Año')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig("./assets/img/hectareasSembradas.png",format='png',dpi=300)
    #plt.show()

    #print(siembraArbolesDF)
    #crearTablaHTML(siembraArbolesDF,"siembraArboles")

    

    

construirDataFrameSiembraArboles()