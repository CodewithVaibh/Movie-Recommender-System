import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies_list=pickle.load(open('movies.pkl','rb'))
movies_list=pd.DataFrame(movies_list)

st.title('Movies Recommender System')

selected_movie = st.selectbox('Select a movie',movies_list['title'].values)

similarity=pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index=movies_list[movies_list['title']==movie].index[0]
    differences=similarity[movie_index]
    list_of_movies=sorted(list(enumerate(differences)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies=[]
    movie_posters=[]
    for i in list_of_movies:
        movies_id=movies_list.iloc[i[0]].id
        movie_posters.append(fetch_poster(movies_id))
        recommended_movies.append((movies_list.iloc[i[0]].title))
    return recommended_movies,movie_posters

if st.button('Recommend'):
    movie_titles,posters=recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       st.text(movie_titles[0])
       st.image(posters[0])

    with col2:
      st.text(movie_titles[1])
      st.image(posters[1])

    with col3:
      st.text(movie_titles[2])
      st.image(posters[2])
      
    with col4:
      st.text(movie_titles[3])
      st.image(posters[3])
      
    with col5:
      st.text(movie_titles[4])
      st.image(posters[4])
      
    with col1:
       st.text(movie_titles[5])
       st.image(posters[5])

    with col2:
      st.text(movie_titles[6])
      st.image(posters[6])

    with col3:
      st.text(movie_titles[7])
      st.image(posters[7])
      
    with col4:
      st.text(movie_titles[8])
      st.image(posters[8])
      
    with col5:
      st.text(movie_titles[9])
      st.image(posters[9])