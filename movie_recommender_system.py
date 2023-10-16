import streamlit as st
import pickle
import pandas as pd
import numpy as np

movie_dict = pickle.load(open('movies_di.pkl', 'rb'))
sim = pickle.load(open('sim.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
st.title('Movie Recommends')
options = st.selectbox('Please Enter a Movie Name',movies['title'].values)

def recommend(movie):
    d=[]
    index1 = movies[movies['title']==movie].index[0]
    movies_list = sorted(list(enumerate(sim[index1])),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        d.append(movies.iloc[i[0]].title) 
    return d

    
if st.button('Recommend'):
    m = recommend(options)
    for i in m:
        st.write(i)
