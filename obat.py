import pickle
import streamlit as st

# membaca model
obat_model = pickle.load(open('obat_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi obat')

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
obat_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi obat'):
    obat_prediction = obat_model.predict([[Umur,Jenis_Kelamin,Tekanan_Darah,Kolestrol,Rasio_Natrium]])

    if obat_diagnosis == 4:
        obat_diagnosis ='Jenis obat DrugY'
    elif obat_diagnosis == 3:
        obat_diagnosis ='Jenis obat drugX'
    elif obat_diagnosis == 2 :
        obat_diagnosis ='Jenis obat drugC'
    elif obat_diagnosis == 1:
        obat_diagnosis ='Jenis obat drugB'
    else:
        obat_diagnosis = 'Jenis obat drugA'

st.success(obat_diagnosis)
