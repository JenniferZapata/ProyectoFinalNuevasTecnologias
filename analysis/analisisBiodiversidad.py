import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorBiodiversidad import generarBiodiversidad
from helpers.generarTabla import crearTablaHTML

#Para analizar datos con python debemos construir un dataframe

def construirDataFrameBiodiversidad():
    #Traigo los datos generados en el Mock
    datosBiodiversidad=generarBiodiversidad()

    #construyo el dataframe
    biodiversidadDF=pd.DataFrame(datosBiodiversidad,columns=['Corregimiento o Comuna','Guardabosques','Cantidad Especies','Especie Predominante'])

      #Limpiando el dataframe
    #1. Limpiando (reemplazando valores)
    #print(biodiversidadDF)
    #biodiversidadDF.replace('-',pd.NA,inplace=True) 
    #biodiversidadDF.replace('sin',pd.NA,inplace=True) 
    
    #2. Limpiando (eliminando valores)
    #biodiversidadDF.replace('sin',pd.NA,inplace=True) 
    #biodiversidadDF.dropna(inplace=True)

    #3. Filtrando datos para depurar la información
    #Filtrar datos es obtener nuevos dataframes al aplicar condiciones logicas, también puede ser contar datos o consultar datos especificos
    #filtroCantidadEspeciesBajo=biodiversidadDF.query("(cantidadEspecies>=1) and (cantidadEspecies<300)")
    #filtroCantidadEspeciesMedio=biodiversidadDF.query("(cantidadEspecies>=300) and (cantidadEspecies<600)")
    #filtroCantidadEspecieAlto=biodiversidadDF.query("(cantidadEspecies>=600)").value_counts()
    
    #print(filtroCantidadEspeciesMedio)
    #print(filtroCantidadEspecieAlto)


    #AGRUPANDO DATOS
    datosAgrupadosG=biodiversidadDF.groupby("Corregimiento o Comuna")["Guardabosques"].mean()
    datosAgrupadosE=biodiversidadDF.groupby("Corregimiento o Comuna")["Cantidad Especies"].mean()
    
    #GRAFICANDO DATOS
    plt.figure(figsize=(20,20))
    datosAgrupadosG.plot(kind='bar',color='yellow')
    plt.title('Cantidad de guardabosques por corregimiento/comuna')
    plt.xlabel('Corregimiento o Comuna')
    plt.ylabel('Guardabosques')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig("./assets/img/guardabosques.png",format='png',dpi=300)
    #plt.show()
    
    # plt.figure(figsize=(20,20))
    # datosAgrupadosE.plot(kind='bar',color='black')
    # plt.title('Cantidad de especies por corregimiento/comuna')
    # plt.xlabel('Corregimiento o Comuna')
    # plt.ylabel('Cantidad Especies')
    # plt.grid(True)
    # plt.xticks(rotation=45)
    # plt.savefig("./assets/img/especies.png",format='png',dpi=300)
    #plt.show()

    #PROBANDO
    #print(biodiversidadDF)
    #crearTablaHTML(biodiversidadDF,"biodiversidad")


construirDataFrameBiodiversidad()