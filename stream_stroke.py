import pickle
import streamlit as st

# Load model
model = pickle.load(open('stroke_model.sav', 'rb'))



# Judul
st.title('Prediksi Penyakit Stroke')
st.write('Gunakan Web ini untuk memprediksi kemungkinan terkena stroke berdasarkan beberapa parameter kesehatan Anda.')

# Input data dari pengguna
gender = st.selectbox('Apa Jenis Kelamin anda?', ['Laki-Laki', 'Perempuan'])

age = st.text_input('Berapa Usia anda?')

hypertension = st.selectbox('Apakah anda mempunyai Darah Tinggi? (Ya: 1 / Tidak: 0)', ['1', '0'])

heart_disease = st.selectbox('Apakah anda mempunyai Penyakit Jantung? (Ya: 1 / Tidak: 0)', ['1', '0'])

ever_married = st.selectbox('Apakah anda Pernah Menikah? (Ya: 1 / Tidak: 0)', ['1', '0'])

avg_glucose_level = st.text_input('Berapa Rata-rata Tinggi Gula anda?')

bmi = st.text_input('Berapa Body Mass Index anda?')

smoking_status = st.selectbox('Apakah anda Merokok? (Ya: 1 / Tidak: 0)', ['1', '0'])

# Pemetaan data kategori ke numerik
categorical_mapping = {
    '1': 1, '0': 0,
    'Laki-Laki': 1, 'Perempuan': 0
}

# Kode prediksi
stroke_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Penyakit Stroke'):
    # Validasi input
    if age == '' or avg_glucose_level == '' or bmi == '':
        st.warning('Mohon isi semua kolom yang diperlukan.')
    else:
            # Konversi input ke tipe data yang sesuai
            age = float(age)
            avg_glucose_level = float(avg_glucose_level)
            bmi = float(bmi)
            
            # Melakukan prediksi
            stroke_prediction = model.predict([[categorical_mapping[gender], age, categorical_mapping[hypertension], categorical_mapping[heart_disease], 
                                                categorical_mapping[ever_married], avg_glucose_level, bmi, categorical_mapping[smoking_status]]])
            if stroke_prediction[0] == 1:
                stroke_diagnosis = 'HATI-HATI!! Pasien terkena Penyakit Stroke'
                st.error(stroke_diagnosis)
            else:
                stroke_diagnosis = 'SELAMAT!! Pasien tidak terkena Penyakit Stroke'
                st.success(stroke_diagnosis)


# Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        © 2024 Hamman Khadafi Al Habibie 21.11.4164
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

# CSS untuk gambar background yang fleksibel
page_bg_img = '''
<style>
.stApp {
  background: url("https://img-cdn.medkomtek.com/IeYHZ_X0Mms5p6WKbg_9lNiBPus=/fit-in/730x411/smart/filters:quality(100):strip_icc():format(webp)/article/Qu6dyehWPrqOsLB5w-1Hz/original/050687900_1572589916-Stroke-infarct-By-peterschreiber.media-Shutterstock_1423084877.jpg") no-repeat center center fixed;
  background-size: contain;
}
</style>
'''

# Menyisipkan CSS ke dalam aplikasi
st.markdown(page_bg_img, unsafe_allow_html=True)
