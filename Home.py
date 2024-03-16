import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.title("Analisis Pengeluaran Masyarakat per Kapita Berdasarkan Bumbu Masak di Provinsi DKI Jakarta 2018-2023")

st.caption("by : [Prayander Sahatma Siahaan](www.linkedin.com/in/prayander-sahatma-siahaan-a481411b6)")

st.header("1. Pendahuluan.")

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
GAR, KEM, KET, MER,  ASA, TER, KEC, MIC, SAJ, SAO, BUJ = st.tabs(["Garam", "Kemiri", "Ketumbar","Merica","Asam","Terasi","Kecap","Micin","Sambal Jadi","Saos Tomat","Bumbu Jadi"])

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Garam.csv'
df = pd.read_csv(df_path)
GAR.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kemiri.csv'
df = pd.read_csv(df_path)
KEM.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_KetumbarJinten.csv'
df = pd.read_csv(df_path)
KET.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstonePPK_MericaLada.csv'
df = pd.read_csv(df_path)
MER.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstonePPK_Asam.csv'
df = pd.read_csv(df_path)
ASA.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstonePPK_Terasi.csv'
df = pd.read_csv(df_path)
TER.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kecap.csv'
df = pd.read_csv(df_path)
KEC.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Micin.csv'
df = pd.read_csv(df_path)
MIC.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SambalJadi.csv'
df = pd.read_csv(df_path)
SAJ.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SaosTomat.csv'
df = pd.read_csv(df_path)
SAO.write(df)

df_path = r'ProjectCapstoneDesign/DatasetProjectCapstone/PPK_BumbuJadi.csv'
df = pd.read_csv(df_path)
BUJ.write(df)

st.caption('Sumber Data : [Badan Pusat Statistik Indonesia.](https://www.bps.go.id/id/statistics-table/2/MjEyMiMy/rata-rata-pengeluaran-perkapita-seminggu--menurut-kelompok-bumbu-bumbuan-per-kabupaten-kota--rupiah-kapita-minggu-.html)')

'''
Untuk menganalisis pengeluaran per kapita masyarakat Indonesia dalam periode 2018-2023 berdasarkan jenis bahan makanan, sampel yang
digunakan adalah data yang terkait dengan provinsi DKI Jakarta di setiap kotanya. DKI Jakarta merupakan wilayah yang sangat representatif
dalam konteks ini karena memiliki beragam karakteristik sosial, ekonomi, dan demografis yang mencerminkan keragaman dalam pola pengeluaran
masyarakat. Dengan fokus pada setiap kota di DKI Jakarta, analisis dapat memberikan wawasan yang lebih mendalam tentang bagaimana pengeluaran
masyarakat berubah dari tahun ke tahun dan bagaimana pola tersebut berkorelasi dengan jenis bahan makanan yang dikonsumsi. Data yang
dikumpulkan dari setiap kota di DKI Jakarta akan memberikan gambaran yang komprehensif tentang tren pengeluaran masyarakat serta
memungkinkan untuk identifikasi perbedaan dan kesamaan dalam pola pengeluaran antar kota. Dengan demikian, analisis ini diharapkan
dapat memberikan wawasan yang berharga bagi pemangku kepentingan dalam merancang kebijakan yang lebih tepat sasaran terkait dengan ketahanan
pangan dan kesejahteraan masyarakat.
'''
col1, col2, col3 = st.columns(3)
with col2:
    st.image(r'ProjectCapstoneDesign/Images/Peta_DKIJakarta.png', 
         caption='Peta Kota di Provinsi DKI Jakarta',
         width=450)
st.header("2. Visualisasi Data.")
st.subheader("2.1. Trend Bumbu Masak setiap kota di Provinsi DKI Jakarta ")
option1 = st.selectbox('Pilih Bumbu Masak :',("Garam", "Kemiri", "Ketumbar","Merica","Asam","Terasi","Kecap","Micin","Sambal Jadi","Saos Tomat","Bumbu Jadi" ), key='option1')

#col1, col2, col3, col4 = st.columns(4)
val_width = 600
val_height = 450

if option1 == "Garam":
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Garam.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran (Rp/Kapita)')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran (Rp/Kapita):Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran (Rp/Kapita):Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Kemiri':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kemiri.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Ketumbar':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_KetumbarJinten.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Merica':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_MericaLada.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Asam':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Asam.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Terasi':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Terasi.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Kecap':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kecap.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Micin':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Micin.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Sambal Jadi':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SambalJadi.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Saos Tomat':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SaosTomat.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass

elif option1 == 'Bumbu Jadi':
    # Load data
    df = pd.read_csv(r"ProjectCapstoneDesign/DatasetProjectCapstone/PPK_BumbuJadi.csv")
    # Define keyword
    keyword = "Jakarta"
    keyword2 = "Seribu"
    # Filter the DataFrame
    filtered_df = df[df['Kabupaten/Kota'].str.contains(keyword, case=False)| df['Kabupaten/Kota'].str.contains(keyword2, case=False)]
    # Melt the DataFrame to make it tidy for Altair
    melted_df = pd.melt(filtered_df, id_vars=['Kabupaten/Kota'], var_name='Tahun', value_name='Pengeluaran')
    # Create the Altair chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x='Tahun:N',
        y='Pengeluaran:Q',
        color='Kabupaten/Kota:N',
        tooltip=['Tahun:N', 'Pengeluaran:Q', 'Kabupaten/Kota:N']
    ).properties(
        width=val_width,
        height = val_height,
        title="Pengeluaran per Kapita untuk " + keyword
    ).interactive()
    # Render the chart
    st.write(chart)
    pass
else:
    pass
