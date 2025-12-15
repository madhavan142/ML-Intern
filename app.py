import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title("📊 Subject Marks Correlation Heatmap")

# Sample dataset
data = {
    "Maths": [80, 90, 85, 70],
    "Physics": [75, 88, 82, 68],
    "Chemistry": [78, 85, 80, 65]
}

df = pd.DataFrame(data)

# Show dataset
st.subheader("Dataset")
st.dataframe(df)

# Correlation matrix
corr = df.corr()

# Plot heatmap
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
