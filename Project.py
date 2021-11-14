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
st.text("I read the 2020 data set, I want to mention that I took 10 000 lines of the csv document,""\n""I do the same with 2016.")


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

# Type local = Maison (Real Estate) _ Code Departement
def ValeurF_CodeP(df):
    trans = df.groupby('code_departement')['type_local=Appartement'].sum().reset_index().sort_values('type_local=Appartement', ascending=False).head(20)
    trans = trans.rename(columns={'type_local=Appartement': 'sum'})
    return trans

############################################################################################################

#partie execution : 

option = st.sidebar.selectbox(
    "Choix de l'année",
    ("2020", "2016"))

if option == "2020":
    st.title("2. Data Traitment")
    st.header("2.1 - Loading The Data")
    #loading the data using this methode
    df_2020=pd.read_csv('https://jtellier.fr/DataViz/full_2016.csv')
    
    st.write(df_2020.head(20))
    df_2020.head(5)
    st.header("2.2 - Cleaning The Database")
    st.markdown("Calculation of the percentage (%) of the NAN values in the Dataset")
    
    #to see the heatmap of the (%) values NAN :
    st.write("Heatmap NAN Values :")
    sns.heatmap(df_2020.isnull(), yticklabels = False, cbar = False)
    st.pyplot()
    st.write("\n")
    st.write("the percentage (%) of the NAN values in the Dataset :")
    df_2020=droping_the_NAN(df_2020)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    
