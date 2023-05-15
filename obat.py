import pickle
import streamlit as st

# membaca model
narkoba_model = pickle.load(open('narkoba_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi narkoba')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Umur = st.text_input ('Input Umur')
    Jenis_Kelamin = st.text_input ('Input Jenis Kelamin (Perempuan = 0, Laki-laki = 1)')
    Tekanan_Darah = st.text_input ('Input Tekanan Darah (Rendah = 0, Normal = 1, Tinggi = 2)')

with col2 :
    Kolestrol = st.text_input ('Input Kolesterol (Normal = 1, Tinggi = 2)')
    Rasio_Natrium = st.text_input ('Input Nilai asio Natrium ke Kalium dalam Darah')

# code untuk prediksi
narkoba_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi narkoba'):
    narkoba_prediction = narkoba_model.predict([[Umur,Jenis_Kelamin,Tekanan_Darah,Kolestrol,Rasio_Natrium]])

    if narkoba_diagnosis == 4:
        narkoba_diagnosis ='Jenis Narkoba DrugY'
    elif narkoba_diagnosis == 3:
        narkoba_diagnosis ='Jenis Narkoba drugX'
    elif narkoba_diagnosis == 2 :
        narkoba_diagnosis ='Jenis Narkoba drugC'
    elif narkoba_diagnosis == 1:
        narkoba_diagnosis ='Jenis Narkoba drugB'
    else:
        narkoba_diagnosis = 'Jenis Narkoba drugA'

st.success(narkoba_diagnosis)
