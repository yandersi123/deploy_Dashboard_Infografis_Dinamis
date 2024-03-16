import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

st.header("2. Visualisasi Data.")
st.subheader("2.1. Trend Bumbu Masak setiap kota di Provinsi DKI Jakarta ")
option1 = st.selectbox('Pilih Bumbu Masak :',("Garam", "Kemiri", "Ketumbar","Merica","Asam","Terasi","Kecap","Micin","Sambal Jadi","Saos Tomat","Bumbu Jadi" ), key='option1')

#col1, col2, col3, col4 = st.columns(4)
val_width = 600
val_height = 450

if option1 == "Garam":
    # Load data
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Garam.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kemiri.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_KetumbarJinten.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_MericaLada.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Asam.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Terasi.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Kecap.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_Micin.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SambalJadi.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_SaosTomat.csv")
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
    df = pd.read_csv("ProjectCapstoneDesign/DatasetProjectCapstone/PPK_BumbuJadi.csv")
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
