import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title(
    "Analisis Pengeluaran Masyarakat per Kapita Berdasarkan Bumbu Masak di Provinsi DKI Jakarta 2018-2023"
    )

st.caption(
    "by : [Prayander Sahatma Siahaan](www.linkedin.com/in/prayander-sahatma-siahaan-a481411b6)"
    )

st.header(
    "1. Pendahuluan."
    )

'''
Ketergantungan masyarakat pada bumbu masak erat terkait dengan pengeluaran per kapita. Bumbu tidak hanya bahan tambahan, 
tetapi juga menentukan kualitas hidangan. Penggunaan bumbu mencerminkan kesejahteraan ekonomi dan preferensi konsumsi. 
Di daerah dengan pengeluaran tinggi, masyarakat memiliki akses lebih besar terhadap berbagai jenis bumbu. Analisis pengeluaran 
per kapita berdasarkan bumbu masak memberikan gambaran tentang pola konsumsi dan ekonomi suatu wilayah. Trend pengeluaran terhadap 
bumbu memberikan informasi tentang preferensi konsumsi dan dinamika ekonomi di Provinsi DKI Jakarta dari 2018-2023.
'''

st.header('Dataset Penelitian.')
'''
Digunakan dataset yang menjelaskan Pengeluaran per kapita masyarakat Indonesia dalam periode 2018-2023 berdasarkan jenis bahan makanan.
Berikut merupakan tabel dataset yang akan digunakan :
'''
GAR, KEM, KET, MER,  ASA, TER, KEC, MIC, SAJ, SAO, BUJ = st.tabs([
    "Garam", 
    "Kemiri", 
    "Ketumbar",
    "Merica",
    "Asam",
    "Terasi",
    "Kecap",
    "Micin",
    "Sambal Jadi",
    "Saos Tomat",
    "Bumbu Jadi"])

df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Garam.csv'
df = pd.read_csv(
    df_path
    )
GAR.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Kemiri.csv'
df = pd.read_csv(
    df_path
    )
KEM.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_KetumbarJinten.csv'
df = pd.read_csv(
    df_path
    )
KET.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_MericaLada.csv'
df = pd.read_csv(
    df_path
    )
MER.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Asam.csv'
df = pd.read_csv(
    df_path
    )
ASA.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Terasi.csv'
df = pd.read_csv(
    df_path
    )
TER.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Kecap.csv'
df = pd.read_csv(
    df_path
    )
KEC.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Micin.csv'
df = pd.read_csv(
    df_path
    )
MIC.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_SambalJadi.csv'
df = pd.read_csv(
    df_path
    )
SAJ.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_SaosTomat.csv'
df = pd.read_csv(
    df_path
    )
SAO.write(df)
df_path = r'C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_BumbuJadi.csv'
df = pd.read_csv(
    df_path
    )
BUJ.write(df)
st.caption(
    'Sumber Data : [Badan Pusat Statistik Indonesia.](https://www.bps.go.id/id/statistics-table/2/MjEyMiMy/rata-rata-pengeluaran-perkapita-seminggu--menurut-kelompok-bumbu-bumbuan-per-kabupaten-kota--rupiah-kapita-minggu-.html)'
    )

st.header(
    "2. Visualisasi Data."
    )
st.subheader(
    "2.1. Trend Bumbu Masak setiap kota di Provinsi DKI Jakarta "
)
option = st.selectbox(
    'Pilih Bumbu Masak :',
    (
        "Garam", 
        "Kemiri", 
        "Ketumbar",
        "Merica",
        "Asam",
        "Terasi",
        "Kecap",
        "Micin",
        "Sambal Jadi",
        "Saos Tomat",
        "Bumbu Jadi" 
        ))

#col1, col2, col3, col4 = st.columns(4)

if option == "Garam":
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Garam.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Garam"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Kemiri':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Kemiri.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Kemiri"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Ketumbar':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_KetumbarJinten.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Ketumbar"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Merica':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_MericaLada.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Merica / Lada"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Asam':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Asam.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Asam"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Terasi':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Terasi.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Terasi"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Kecap':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Kecap.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = 'Pengeluaran per Kapita untuk Kecap'
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Micin':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_Micin.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Micin"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Sambal Jadi':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_SambalJadi.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Sambal Jadi"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Saos Tomat':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_SaosTomat.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Saos Tomat"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

elif option == 'Bumbu Jadi':
    df = pd.read_csv(r"C:\Users\siaha\Documents\TETRIS 4\ProjectCapstoneDesign\DatasetProjectCapstone\PPK_BumbuJadi.csv")
    keyword = "Jakarta"
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)]
    
    # Buat line chart dengan Plotly
    fig = go.Figure()

    for index, row in filtered_df.iterrows():
        fig.add_trace(go.Scatter(x=filtered_df.columns[1:], y=row[1:], mode='lines+markers', name=row['Kabupaten/Kota']))

    titl = "Pengeluaran per Kapita untuk Bumbu Jadi"
    fig.update_layout(title=titl, xaxis_title='Tahun', yaxis_title='Pengeluaran (Rp/Kapita)')
    st.plotly_chart(fig)
    pass

else:
    pass

#st.subheader(
#   "2.2. Rating Tertinggi Bumbu Masak "
#)

#option = st.selectbox(
#    'Pilih Tahun :',
#    (
#        "2018",
#        "2019",
#        "2020",
#        "2021",
#        "2022",
#        "2023" 
#        ))

#col1, col2, col3, col4 = st.columns(4)
#st.header(
#    "3. Insight."
#    )
#
#st.subheader(
#    "3.1. Insight untuk Poin 2.1"
#)
