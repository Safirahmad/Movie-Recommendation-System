import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/{ }?api_key=b1975b06e8c096a044bb0aed42b05c1a'.format(movie_id))
    data=response.json()
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movie=[]
    for i in movies_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie    
    
similarity=movies_dict=pickle.load(open('similarity.pkl','rb'))

movies_dict=pickle.load(open('movies_dic.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title("Movie Recommendation")
selected_movies_name = st.selectbox(
'How would you now to connected',
movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movies_name)
    for i in recommendations:
        st.write(i)