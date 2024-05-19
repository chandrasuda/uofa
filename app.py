import streamlit as st
import joblib
import numpy as np
import librosa
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt


# Load the joblib model
model = joblib.load('Jan-25-model.joblib')

# Set the app title
st.set_page_config(page_title='TB Detection from Cough Audio')
st.title('TB Detection for Cough Audio')
st.write('This app is for detecting TB from cough audio.')

# Audio file upload
audio_file = st.file_uploader('Upload Audio File', type=['wav', 'mp3'])

# Demographic inputs
sex = st.selectbox('Sex', ['Male', 'Female'])
age = st.number_input('Age', min_value=0, max_value=150, value=30)
height = st.number_input('Height (cm)', min_value=0, max_value=300, value=170)
weight = st.number_input('Weight (kg)', min_value=0, max_value=500, value=70)
reported_cough_dur = st.number_input('Reported Cough Duration (days)', min_value=0, value=7)
tb_prior = st.selectbox('TB Prior', ['Yes', 'No'])
tb_prior_Pul = st.selectbox('TB Prior (Pulmonary)', ['Yes', 'No'])
tb_prior_Extrapul = st.selectbox('TB Prior (Extrapulmonary)', ['Yes', 'No'])
tb_prior_Unknown = st.selectbox('TB Prior (Unknown)', ['Yes', 'No'])
hemoptysis = st.selectbox('Hemoptysis', ['Yes', 'No'])
heart_rate = st.number_input('Heart Rate', min_value=0, max_value=300, value=80)
temperature = st.number_input('Temperature (°C)', min_value=0.0, max_value=50.0, value=37.0)
weight_loss = st.selectbox('Weight Loss', ['Yes', 'No'])
smoke_lweek = st.selectbox('Smoke last week)', ['Yes', 'No'])
fever = st.selectbox('Fever', ['Yes', 'No'])
night_sweats = st.selectbox('Night Sweats', ['Yes', 'No'])

# Function to read audio file
def read_audio(x):
    y = librosa.load(x)[0]
    return librosa.util.fix_length(y, size=11025)

def calc_mel_spectrogram(y, sr = 22050, n_fft = 2048, hop_length = 512, n_mels=128):
    spect = librosa.feature.melspectrogram(y=y, n_fft=n_fft, sr=sr, hop_length=hop_length, n_mels = n_mels)
    return librosa.power_to_db(spect, ref=np.max)
    

# Function to run prediction
def predict_single_audio(audio_file, demographic_data):
    # read audio file
    audio = read_audio(audio_file)
    mel_spectrogram = calc_mel_spectrogram(audio)

    # demographic data
    demographic_data = [0 if x == 'Male' else 1 if x == 'Female' else x for x in demographic_data]
    demographic_data = [0 if x == 'No' else 1 if x == 'Yes' else x for x in demographic_data]
    demographic_data = np.array(demographic_data)  
    
    # predict
    prediction = model.predict({'mel_input': np.array([mel_spectrogram]), 'tabular_input': np.array([demographic_data])})
    st.write('Your probability of being TB positive:', prediction[0][0])
    # print negative or positive
    if prediction[0][0] < 0.5:
        st.write('The model classifies you as TB NEGATIVE.')
    else:
        st.write('The model classifies you as TB POSITIVE.')

   # display mel-spectrogram image of their cough
    st.audio(audio_file)
    st.write('Your cough mel-spectrogram:')
    fig, ax = plt.subplots(figsize=(10, 4))
    # Display the mel spectrogram with librosa
    img = librosa.display.specshow(mel_spectrogram, y_axis='mel', x_axis='time', cmap='viridis', auto_aspect=True, ax=ax)
    plt.colorbar(img, format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.tight_layout()
    st.pyplot(fig)
        

        

# One-hot encode demographic data
demographic_data = [sex, age, height, weight, reported_cough_dur, tb_prior, tb_prior_Pul, tb_prior_Extrapul, tb_prior_Unknown, hemoptysis, heart_rate, temperature, weight_loss, smoke_lweek, fever, night_sweats]

# Submit button
if st.button('Submit'):
    predict_single_audio(audio_file, demographic_data)
    




