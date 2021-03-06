from IPython.display import display
from matplotlib import pyplot as plt
import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
import altair as alt
import timeit
import math
import streamlit as st
import os



st.title("Projet : Data Visualisation")

st.text("Author : Anas Zaghloul, M1 BD-APP")
#What are the cities or departments that have esperienced the biggest price increase this year? the last 4 years ?
# means I'm going to analyse the 2020 document and the 2016 document ( maybe combine 2 samples of them and then analyze them)
"\n"

st.title("1 - Main Idea of my project")

"\n"
st.write("Nous pourrons savoir aussi à partir de ce jeu de données l'évoution selon le temps ( entre 2016 et 2020 ) pour chaque type de biens. Le point faible de ce jeu, c'est qu'il n'y a pas mal des informations manquantes (comme les caractéristiques du bien, le nombre d'étage, ascenseur, année de construction ...")




data_url_2020 = 'https://jtellier.fr/DataViz/full_2020.csv'
data_url_2016 = 'https://jtellier.fr/DataViz/full_2016.csv'
data_url_2018 = 'https://jtellier.fr/DataViz/full_2018.csv'
data_url_2019 = 'https://jtellier.fr/DataViz/full_2019.csv'

def load_data(url):
    df = pd.read_csv(url, low_memory=False, nrows = 300000)
    return df


#fuction that calculate the % of NAN values in the dataset : if it's more that 75% we drop them ! 
def droping_the_NAN(df):
    new_df= df
    col_to_drop = []
    for col in new_df.columns:
        
        missing = round((new_df[col].isna().sum()*100)/len(new_df[col]), 2)
        st.write("  {}   {}% " .format(col, missing))
        if missing > 75:
            col_to_drop.append(col)
    return df.drop(col_to_drop, axis=1, inplace=True)

def drop_dataNA(dfa):
    dfa = dfa.dropna()
    return dfa

#the columns to drop because of there 75% of NAN values :
def col_to_drop(df):
    droping_the_NAN(df)
    return col_to_drop

#Now let's Drop these columns with this fuction !
def drop_the_col(df_nan):
    df_nan = df_nan.dropna(how="all")
    return df_nan


#Now let's drop the duplicated values :
def duplicated_values(df):
    #let's the number of duplicated values:
    st.write("the duplicated values = '",df.duplicated().sum())
    st.write("\n")
    df = df.drop_duplicates()
    #let's check their numbers again !
    st.write("the duplicated values = '",df.duplicated().sum())
    st.write("\n")
    return df

def corrmat(df):
    return df.corr()

############# fonction pour le traitement des vizuels : 

#valeur foncière_ Code_departement:

def ValeurF_CodeP(df):
    trans = df.groupby('code_departement')['valeur_fonciere'].sum().reset_index().sort_values('valeur_fonciere', ascending=False).head(20)
    trans = trans.rename(columns={'valeur_fonciere': 'sum'})
    return trans

#Valeur Foncière _ nature culture

def ValeurF_NatureC(df):
    trans = df.groupby('nature_culture')['valeur_fonciere'].sum().reset_index().sort_values('valeur_fonciere', ascending=False).head(6)
    trans = trans.rename(columns={'valeur_fonciere': 'sum'})
    return trans


#Valeur Foncière _ Nb pièces

def ValeurF_NombrePP(df):
    trans = df.groupby('nombre_pieces_principales')['valeur_fonciere'].sum().reset_index().sort_values('valeur_fonciere', ascending=False).head(6)
    trans = trans.rename(columns={'valeur_fonciere': 'sum'})
    return trans

#Surface _ Code Departement

def transform_Codp_Surface(df):
    nature = df.groupby('code_commune')['surface_terrain'].sum().reset_index().sort_values('surface_terrain', ascending=False).head(20)
    nature = nature.rename(columns={'surface_terrain': 'sum'})
    return nature

############################################################################################################

#partie execution : 

option = st.sidebar.selectbox(
    "Choix de l'année",
    ("2020", "2019","2018","2016"))

if option == "2020":
    st.title("2. Data Traitment")
    st.header("2.1 - Loading The Data")
    #loading the data using this methode
    df_2020=load_data(data_url_2020)
    
    st.write(df_2020.head(20))
    df_2020.head(5)
    st.header("2.2 - Cleaning The Database")
    st.markdown("Calculation of the percentage (%) of the NAN values in the Dataset")
    
    #to see the heatmap of the (%) values NAN :
    st.write("Heatmap NAN Values : (before the transformation of our dataset)")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    sns.heatmap(df_2020.isnull(), yticklabels = False, cbar = False)
    st.pyplot()
    st.write("\n")
    st.write("the percentage (%) of the NAN values in the Dataset :")

    droping_the_NAN(df_2020)
    df_2020=drop_dataNA(df_2020)
    st.write("\n")
    df_2020=duplicated_values(df_2020)

    #traitement du type : 
    #df_2020['lot1_numero'] = df_2020['lot1_numero'].astype('object')
    df_2020['code_postal'] = df_2020['code_postal'].astype('object')
    df_2020['code_type_local'] = df_2020['code_type_local'].astype('object')
    df_2020['type_local'] = df_2020['type_local'].astype('object')
    df_2020['nombre_pieces_principales'] = df_2020['nombre_pieces_principales'].astype(
    'object')
    df_2020['code_departement'] = df_2020['code_departement'].astype('object')
    df_2020['code_commune'] = df_2020['code_commune'].astype('object')
    df_2020['nombre_lots'] = df_2020['nombre_lots'].astype('float64')
    df_2020['latitude'] = pd.to_numeric(df_2020['latitude'])
    df_2020['longitude'] = pd.to_numeric(df_2020['longitude'])

    st.markdown("Maintenant aprés la supression  :")
    st.write("- Des valeurs des colonnes à 75% valeurs NAN")
    st.write("- Des doublons")
    st.write(df_2020.astype(object))
    #to see the heatmap of the (%) values with NAN values :
    st.write("Heatmap NAN Values : ( before the transformation of our dataset")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.heatmap(df_2020.isnull(), yticklabels=False, cbar=False)
    st.pyplot()

    #partie traitement des données : 

    st.title("Data Visualization")

    st.markdown("Valeur foncière ET Code Du Département :")

    #valeur foncière_ Code_departement:
    ValeurF_CodeP(df_2020).plot.bar(x='code_departement', y='sum', color=['green', 'yellow'])
    st.pyplot()

        
    st.markdown("2 .Nature culture et valuer foncière :")


    ValeurF_NatureC(df_2020).plot.bar(x="nature_culture", y="sum")
    st.pyplot()


    st.markdown("3 .Nature culture et valuer foncière :")
    #Valeur Foncière _ Nb pièces
    ValeurF_NombrePP(df_2020).plot.bar(x="nombre_pieces_principales", y="sum")
    st.pyplot()

    
    st.markdown("4 .code postal _ Surface :")
    #code postal _ Surface :
    transform_Codp_Surface(df_2020).plot.bar(x='code_commune', y='sum', color=['orange', 'green'])
    st.pyplot()

    if st.checkbox("Please click to see the corr matrice "):
        #matrice corr : 
        st.header("Matrice de corrélation : ")
        sns.heatmap(corrmat(df_2020), vmax=.9, square=True) 
        st.pyplot()
 
    ####2016:
    
    
elif option == "2016":
    st.title("2. Data Traitment")
    st.header("2.1 - Loading The Data")
    #loading the data using this methode
    df_2016=load_data(data_url_2016)

    st.write(df_2016.head(20))
    df_2016.head(5)
    st.header("2.2 - Cleaning The Database")
    st.markdown("Calculation of the percentage (%) of the NAN values in the Dataset")
    
    #to see the heatmap of the (%) values NAN :
    st.write("Heatmap NAN Values : (before the transformation of our dataset)")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    sns.heatmap(df_2016.isnull(), yticklabels = False, cbar = False)
    st.pyplot()
    st.write("\n")
    st.write("the percentage (%) of the NAN values in the Dataset :")

    droping_the_NAN(df_2016)
    df_2016=drop_dataNA(df_2016)
    st.write("\n")
    df_2016=duplicated_values(df_2016)

    #traitement du type : 
    #df_2020['lot1_numero'] = df_2020['lot1_numero'].astype('object')
    df_2016['code_postal'] = df_2016['code_postal'].astype('object')
    df_2016['code_type_local'] = df_2016['code_type_local'].astype('object')
    df_2016['type_local'] = df_2016['type_local'].astype('object')
    df_2016['nombre_pieces_principales'] = df_2016['nombre_pieces_principales'].astype(
    'object')
    df_2016['code_departement'] = df_2016['code_departement'].astype('object')
    df_2016['code_commune'] = df_2016['code_commune'].astype('object')
    df_2016['nombre_lots'] = df_2016['nombre_lots'].astype('float64')
    df_2016['latitude'] = pd.to_numeric(df_2016['latitude'])
    df_2016['longitude'] = pd.to_numeric(df_2016['longitude'])

    st.markdown("Maintenant aprés la supression  :")
    st.write("- Des valeurs des colonnes à 75% valeurs NAN")
    st.write("- Des doublons")
    st.write(df_2016.astype(object))
    #to see the heatmap of the (%) values with NAN values :
    st.write("Heatmap NAN Values : ( before the transformation of our dataset")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.heatmap(df_2016.isnull(), yticklabels=False, cbar=False)
    st.pyplot()

    #partie traitement des données : 

    st.title("Data Visualization")

    st.markdown("1. Valeur foncière ET Code Du Département :")

    #valeur foncière_ Code_departement:
    ValeurF_CodeP(df_2016).plot.bar(x='code_departement', y='sum', color=['green', 'yellow'])
    st.pyplot()

    
    st.markdown("2 .Nature culture et valuer foncière :")


    ValeurF_NatureC(df_2016).plot.bar(x="nature_culture", y="sum")
    st.pyplot()


    st.markdown("3 .Nature culture et valuer foncière :")
    #Valeur Foncière _ Nb pièces
    ValeurF_NombrePP(df_2016).plot.bar(x="nombre_pieces_principales", y="sum")
    st.pyplot()

    

    #code postal _ Surface :
    transform_Codp_Surface(df_2016).plot.bar(x='code_commune', y='sum', color=['orange', 'green'])
    st.pyplot()


    #matrice corr : 
    
    if st.checkbox("Please click to see the corr matrice "):
        #matrice corr : 
        st.header("Matrice de corrélation")
        sns.heatmap(corrmat(df_2016), vmax=.9, square=True) 
        st.pyplot()
        
   ###2018

elif option == "2018":
    st.title("2. Data Traitment")
    st.header("2.1 - Loading The Data")
    #loading the data using this methode
    df_2018=load_data(data_url_2018)

    st.write(df_2018.head(20))
    df_2018.head(5)
    st.header("2.2 - Cleaning The Database")
    st.markdown("Calculation of the percentage (%) of the NAN values in the Dataset")
    
    #to see the heatmap of the (%) values NAN :
    st.write("Heatmap NAN Values : (before the transformation of our dataset)")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    sns.heatmap(df_2018.isnull(), yticklabels = False, cbar = False)
    st.pyplot()
    st.write("\n")
    st.write("the percentage (%) of the NAN values in the Dataset :")

    droping_the_NAN(df_2018)
    df_2018=drop_dataNA(df_2018)
    st.write("\n")
    df_2018=duplicated_values(df_2018)

    #traitement du type : 
    df_2018['code_postal'] = df_2018['code_postal'].astype('object')
    df_2018['code_type_local'] = df_2018['code_type_local'].astype('object')
    df_2018['type_local'] = df_2018['type_local'].astype('object')
    df_2018['nombre_pieces_principales'] = df_2018['nombre_pieces_principales'].astype(
    'object')
    df_2018['code_departement'] = df_2018['code_departement'].astype('object')
    df_2018['code_commune'] = df_2018['code_commune'].astype('object')
    df_2018['nombre_lots'] = df_2018['nombre_lots'].astype('float64')
    df_2018['latitude'] = pd.to_numeric(df_2018['latitude'])
    df_2018['longitude'] = pd.to_numeric(df_2018['longitude'])

    st.markdown("Maintenant aprés la supression  :")
    st.write("- Des valeurs des colonnes à 75% valeurs NAN")
    st.write("- Des doublons")
    st.write(df_2018.astype(object))
    #to see the heatmap of the (%) values with NAN values :
    st.write("Heatmap NAN Values : ( before the transformation of our dataset")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.heatmap(df_2018.isnull(), yticklabels=False, cbar=False)
    st.pyplot()

    #partie traitement des données : 

    st.title("Data Visualization")

    st.markdown("1. Valeur foncière ET Code Du Département :")

    #valeur foncière_ Code_departement:
    ValeurF_CodeP(df_2018).plot.bar(x='code_departement', y='sum', color=['green', 'yellow'])
    st.pyplot()

    
    st.markdown("2 .Nature culture et valuer foncière :")


    ValeurF_NatureC(df_2018).plot.bar(x="nature_culture", y="sum")
    st.pyplot()


    st.markdown("3 .Nature culture et valuer foncière :")
    #Valeur Foncière _ Nb pièces
    ValeurF_NombrePP(df_2018).plot.bar(x="nombre_pieces_principales", y="sum")
    st.pyplot()

    

    #code postal _ Surface :
    transform_Codp_Surface(df_2018).plot.bar(x='code_commune', y='sum', color=['orange', 'green'])
    st.pyplot()

    if st.checkbox("Please click to see the corr matrice "):
        #matrice corr : 
        st.header("Matrice de corrélation : ")
        sns.heatmap(corrmat(df_2018), vmax=.9, square=True) 
        st.pyplot()
        
  ###2019 :

elif option == "2019":
    st.title("2. Data Traitment")
    st.header("2.1 - Loading The Data")
    #loading the data using this methode
    df_2019=load_data(data_url_2019)

    st.write(df_2019.head(20))
    df_2019.head(5)
    st.header("2.2 - Cleaning The Database")
    st.markdown("Calculation of the percentage (%) of the NAN values in the Dataset")
    
    #to see the heatmap of the (%) values NAN :
    st.write("Heatmap NAN Values : (before the transformation of our dataset)")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    sns.heatmap(df_2019.isnull(), yticklabels = False, cbar = False)
    st.pyplot()
    st.write("\n")
    st.write("the percentage (%) of the NAN values in the Dataset :")

    droping_the_NAN(df_2019)
    df_2019=drop_dataNA(df_2019)
    st.write("\n")
    df_2019=duplicated_values(df_2019)

    #traitement du type : 
    df_2019['code_postal'] = df_2019['code_postal'].astype('object')
    df_2019['code_type_local'] = df_2019['code_type_local'].astype('object')
    df_2019['type_local'] = df_2019['type_local'].astype('object')
    df_2019['nombre_pieces_principales'] = df_2019['nombre_pieces_principales'].astype(
    'object')
    df_2019['code_departement'] = df_2019['code_departement'].astype('object')
    df_2019['code_commune'] = df_2019['code_commune'].astype('object')
    df_2019['nombre_lots'] = df_2019['nombre_lots'].astype('float64')
    df_2019['latitude'] = pd.to_numeric(df_2019['latitude'])
    df_2019['longitude'] = pd.to_numeric(df_2019['longitude'])

    st.markdown("Maintenant aprés la supression  :")
    st.write("- Des valeurs des colonnes à 75% valeurs NAN")
    st.write("- Des doublons")
    st.write(df_2019.astype(object))
    #to see the heatmap of the (%) values with NAN values :
    st.write("Heatmap NAN Values : ( before the transformation of our dataset")

    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.heatmap(df_2019.isnull(), yticklabels=False, cbar=False)
    st.pyplot()

    #partie traitement des données : 

    st.title("Data Visualization")

    st.markdown("1. Valeur foncière ET Code Du Département :")

    #valeur foncière_ Code_departement:
    ValeurF_CodeP(df_2019).plot.bar(x='code_departement', y='sum', color=['green', 'yellow'])
    st.pyplot()

    
    st.markdown("2 .Nature culture et valuer foncière :")


    ValeurF_NatureC(df_2019).plot.bar(x="nature_culture", y="sum")
    st.pyplot()


    st.markdown("3 .Nature culture et valuer foncière :")
    #Valeur Foncière _ Nb pièces
    ValeurF_NombrePP(df_2019).plot.bar(x="nombre_pieces_principales", y="sum")
    st.pyplot()

    

    #code postal _ Surface :
    transform_Codp_Surface(df_2019).plot.bar(x='code_commune', y='sum', color=['orange', 'green'])
    st.pyplot()

    if st.checkbox("Please click to see the corr matrice "):
        #matrice corr : 
        st.header("Matrice de corrélation : ")
        sns.heatmap(corrmat(df_2019), vmax=.9, square=True) 
        st.pyplot()

