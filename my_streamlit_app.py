import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Quest on Streamlit : build and share data apps!')

link_cars = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
data_cars = pd.read_csv(link_cars)
df_cars = pd.DataFrame(data_cars)
df_cars.info()

# Obtenez la liste complète des continents disponibles
all_continents = df['continent'].unique()

# Ajouter des boutons pour filtrer par continent avec tous les continents sélectionnés par défaut
st.sidebar.header('Filtrer par continent')
continents = st.sidebar.multiselect('Sélectionner les continents:', all_continents, default=all_continents)

# Appliquer le filtre à l'ensemble du DataFrame
filtered_df = df[df['continent'].isin(continents) if continents else True]

st.title("Here's the DataFrame!")
df_cars

st.title("Here's the pairplot!")
viz_correlation = sns.heatmap(df_cars.select_dtypes("number").corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
st.pyplot(viz_correlation.figure)

st.title("Here's the scatterplots!")
unique_continents = df_cars['continent'].unique().tolist()
selected_continents = st.multiselect("Choose continent", unique_continents)

st.subheader("Scatterplot: MPG vs HP")
st.scatter_chart(filtered_data, x="mpg", y="hp", color="continent")
