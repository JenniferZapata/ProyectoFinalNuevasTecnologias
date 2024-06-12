import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML

#Para analizar datos con python debemos construir un dataframe

def construirDataFrameCalidadAire():
    #Traigo los datos generados en el Mock
    datosCalidadAire=generarDatosCalidadAire()

    #construyo el dataframe
    calidadAireDF=pd.DataFrame(datosCalidadAire,columns=['Comuna','Total Poblacion','Tamaño Muestra','ICA','Fecha','Nombre','ID'])

    #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    #print(calidadAireDF)
    #calidadAireDF.replace('-',pd.NA,inplace=True) 
    #calidadAireDF.replace('sin',pd.NA,inplace=True) 

    #2. Limpiando (eliminando valores)
    calidadAireDF.replace('sin',pd.NA,inplace=True) 
    calidadAireDF.dropna(inplace=True)
    

    #3. Filtrando datos para depurar la información
    #Filtrar datos es obtener nuevos dataframes al aplicar condiciones logicas, también puede ser contar datos o consultar datos especificos
    #filtroICAPositivo=calidadAireDF.query("(ICA>=20) and (ICA<50)")
    #filtroICAModerado=calidadAireDF.query("(ICA>=50) and (ICA<70)")
    #filtroICAPeligroso=calidadAireDF.query("(ICA>=70)").value_counts()

    #print(filtroICAPositivo)
    #print("\n")
    #print(filtroICAModerado)
    #print("\n")
    #print(filtroICAPeligroso)

    #AGRUPANDO DATOS
    datosAgrupados=calidadAireDF.groupby("Comuna")["ICA"].mean()
    
    #GRAFICANDO DATOS
    plt.figure(figsize=(20,20))
    datosAgrupados.plot(kind='bar',color='green')
    plt.title('Calidad de aire por comuna en Medellin')
    plt.xlabel('Comuna')
    plt.ylabel('ICA (Indice de calidad de Aire)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig("./assets/img/calidadAire.png",format='png',dpi=300)
    #plt.show()

    #Probando
    #print("\n")
    #print(calidadAireDF)
    #crearTablaHTML(calidadAireDF,"calidadAire")

construirDataFrameCalidadAire()