import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

data = pd.read_csv('datafinal.csv')
data['dteday'] = pd.to_datetime(data['dteday'])

min_date = data['dteday'].min()
max_date = data['dteday'].max()

with st.sidebar:
    # Menambahkan gambar
    st.image("bicycle.jpg")
    st.subheader('Bike Sharing Corp.')
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
main_df = data[(data["dteday"] >= str(start_date)) & 
                (data["dteday"] <= str(end_date))]

st.header('Data Visualization: Bike Sharing')

# Membuat visualisasi pertama
st.subheader('User Comparison in Weekdays')

col1, col2 = st.columns(2)

with col1:
    average_customer_per_day = round(main_df['casual'].mean())
    st.metric("Average Casual Customer per Day", value=str(average_customer_per_day))

with col2:
    average_customer_per_day = round(main_df['registered'].mean())
    st.metric("Average Registered Customer per Day", value=str(average_customer_per_day))

fig, ax = plt.subplots(1,2, figsize=(10,4))
sns.barplot(x='weekday', y='casual', data=main_df, ax = ax[0], palette='muted')
sns.barplot(x='weekday', y='registered', data=main_df, ax = ax[1], palette='muted')

ax[0].set_xlabel('')
ax[1].set_xlabel('')
ax[0].set_ylabel('')
ax[1].set_ylabel('')
ax[0].set_title('Casual')
ax[1].set_title('Registered')

common_ylim = max(ax[0].get_ylim()[1], ax[1].get_ylim()[1])
ax[0].set_ylim(0, common_ylim)
ax[1].set_ylim(0, common_ylim)

st.pyplot(fig)

# Membuat visualisasi kedua
st.subheader('Customer Count by Month')

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(x='mnth', y='cnt', data=main_df, hue='yr', ax=ax, palette='deep')
plt.legend(title='Year', title_fontsize='12')
ax.set_xlabel('')
ax.set_ylabel('')

st.pyplot(fig)

# Membuat visualisasi ketiga
st.subheader('Customer Count Comparison by Working Day')

fig, ax = plt.subplots(figsize=(11, 6))
sns.barplot(x='hr', y='cnt', data=main_df, ax=ax, hue='workingday', palette='husl')
plt.legend(title='Working Day', title_fontsize='12')

ax.set_xlabel('Hours in Day')
ax.set_ylabel('')

st.pyplot(fig)


