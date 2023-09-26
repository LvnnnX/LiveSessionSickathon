import streamlit as st  
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from utils import visualize_type
import altair as alt

url: str = 'https://docs.google.com/spreadsheets/d/1XoifLF-7fW1Gb6HNiFvNHix4Grnox0UJecOGwVbaOl8/edit?usp=sharing'
conn: GSheetsConnection = st.experimental_connection('netflix_titles', type=GSheetsConnection)

df: pd.DataFrame = conn.read(spreadsheet=url, worksheet=0)


st.header('Netflix Analysis')
st.subheader('Raw Data From Google Sheets')
st.write('Data mentah dari Google Sheets yang diambil dari kaggle')
st.dataframe(df)

st.divider()
st.subheader('Netflix Type Distribution')
st.write('Persebaran tipe netflix (Movies atau TV Show) dari data mentah')
# st.dataframe(visualize_type(df))
st.pyplot(visualize_type(df))

st.divider()
st.subheader('Top 10 Movies Countries')
st.write('Top 10 negara dengan jumlah produksi movies terbanyak')

top_10_countries_movies: pd.DataFrame = df[df['type']=='Movie']['country'].value_counts().head(10).reset_index()

movie_chart = (
    alt.Chart(top_10_countries_movies).mark_bar().encode(
        x=alt.X('index', sort='-y'),
        y=alt.Y('country')
    )
)

# st.dataframe(top_10_countries_movies)
st.altair_chart(movie_chart, use_container_width=True)


st.divider()
st.subheader('Release year distribution')
st.write('Perseabran tahun rilis dari data Netflix Titles')

tahun_rilis: pd.DataFrame = df[['release_year','type']].value_counts().sort_index().unstack()
st.bar_chart(tahun_rilis)

st.divider()
st.subheader('Top 10 Genres on Netflix')
st.write('Top 10 Genre dengan jumlah produksi terbanyak')
top_10_genres: pd.DataFrame = df['listed_in'].apply(lambda x: x.replace(' ,',',').replace(', ',',').split(','))
Genres:list = []
for i in top_10_genres: Genres += i
Genres: pd.DataFrame = pd.DataFrame(Genres, columns=['Genre']).value_counts().head(10).reset_index()
Genres.columns = ['Genre', 'Count']

genres_chart = (
    alt.Chart(Genres).mark_bar().encode(
        x=alt.X('Genre', sort='-y'),
        y=alt.Y('Count')
    )
)

# st.dataframe(Genres)

st.altair_chart(genres_chart, use_container_width=True)