import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Quest on Streamlit : build and share data apps!')

link_cars = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
data_cars = pd.read_csv(link_cars)

try:
	df_cars = pd.DataFrame(data_cars)

	# Obtenez la liste complète des continents disponibles
	all_continents = df_cars ['continent'].unique()

	# Ajouter des boutons pour filtrer par continent avec tous les continents sélectionnés par défaut
	st.sidebar.header('Filtrer par continent')
	continents = st.sidebar.multiselect('Sélectionner les continents:', all_continents, default=all_continents)

	if not continents:
        	st.error("Please select at least one continent.")

	else:

		# Appliquer le filtre à l'ensemble du DataFrame
		filtered_df = df_cars [df_cars ['continent'].isin(continents) if continents else True]

		st.title("Here's the DataFrame!")
		df_cars

		st.title("Here's the pairplot!")
		viz_correlation = sns.heatmap(df_cars.select_dtypes("number").corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
		st.pyplot(viz_correlation.figure)

		st.title("Here's the scatterplot!")

		st.subheader("Scatterplot: MPG vs HP")
		st.scatter_chart(filtered_df, x="mpg", y="hp", color="continent")

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
