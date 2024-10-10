import streamlit as st
import pandas as pd
import plotly.express as px

# Load the datasets
data = pd.read_csv('github_dataset.csv')
repo_data = pd.read_csv('repository_data.csv')

combined_data = pd.concat([data, repo_data], ignore_index=True)

st.markdown( 
    """
    <style>
    .reportview-container {
        background: #f0f2f5;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Header
st.title("🌟 GitHub Repositories Dashboard")
st.header("Insights and Visualizations")
st.image("WHITE-NO-BACKGROUND.png", width=700)

# Display the combined dataset
st.subheader("Combined Dataset Overview")
st.write(
    "This section provides an overview of the combined GitHub dataset, displaying the first few entries for review."
)
st.dataframe(combined_data.head())

# Bar chart of repository languages
language_count = combined_data['language'].value_counts()
st.subheader("Repositories by Language")
st.write(
    "This bar chart visualizes the number of repositories for each programming language used in the dataset."
)
st.bar_chart(language_count)

# Pie chart for better visual representation
st.subheader("Language Distribution")
st.write(
    "The pie chart below illustrates the distribution of repositories by programming language, providing a clear visual understanding."
)
fig = px.pie(names=language_count.index, values=language_count.values, title="Repositories by Language")
st.plotly_chart(fig)

# Dropdown for selecting a programming language
selected_language = st.selectbox("Select a programming language:", combined_data['language'].unique())
filtered_data = combined_data[combined_data['language'] == selected_language]

# Show the filtered data
st.subheader(f"Filtered Data for {selected_language}")
st.write(
    f"This table displays the repositories that are specifically using **{selected_language}**."
)
st.dataframe(filtered_data)
