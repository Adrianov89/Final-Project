import streamlit as st
import pickle
import pandas as pd
import numpy as np

#Load the pickled model
with open('KNN_Model.pkl', 'rb') as model_file:
     model = pickle.load(model_file)


st.title('Ready for Success! :sound:')

col1, col2, col3 = st.columns(3)

with col1:
    duration_ms = st.number_input('Duration (Seconds)', 200) * 1000
    acousticness = st.slider('Acousticness', 0.0,1.0, 0.01)
    danceability = st.slider('Danceability', 0.0,1.0, 0.51) 
    

with col2:
    mode = st.selectbox('Mode', [0,1])
    energy = st.slider('Energy', 0.0,1.0, 0.73)
    instrumentalness = st.slider('Instrumentalness', 0.0,1.0, 0.01)
    key = st.slider('Key', 0,11)


with col3:
    tempo = st.number_input('Tempo', 1)
    speechiness = st.slider('Speechiness', 0.0,1.0, 0.05)
    liveness = st.slider('Liveness', 0.0,1.0, 0.08)
    valence = st.slider('Valence', 0.0,1.0, 0.33)

features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness", "key", "liveness", 
            "mode", "speechiness", "tempo", "valence"]

def predict():
    row = np.array([acousticness, danceability, duration_ms, energy, instrumentalness, key, liveness, mode, speechiness, tempo, valence])
    X = pd.DataFrame([row], columns=features)
    prediction = model.predict(X)[0]

    if prediction == 1:
         #st.success('It will be the next BIG HIT !!!!! 🎸🎷🥁🎺🎶')
         st.markdown('<p style="font-size:24px; color:green;">It will be the next CHART-TOPPING HIT !!!!! 🎸🎷🥁🎺🎙️</p>', unsafe_allow_html=True)
    else:
         st.markdown('<p style="font-size:24px; color:red;">Not good enough... 💩💩💩💩💩</p>', unsafe_allow_html=True)


st.button('Popular or not?', on_click = predict)


