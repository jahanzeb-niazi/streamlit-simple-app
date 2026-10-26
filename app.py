import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA App", layout="wide")

st.title("Exploratory Data Analysis Interface")

# ---------- Sidebar: all controls ----------
st.sidebar.title("Dataset Controls")
file = st.sidebar.file_uploader("Upload CSV File for Analysis", type=["csv"])

if file is None:
    st.write("Please upload a CSV file from the sidebar. (Test with titanic.csv)")
else:
    df = pd.read_csv(file)
    st.sidebar.success("File uploaded successfully")

    # ---------- Top section: preview + metadata ----------
    st.write("### Dataset Preview & Metadata")

    st.write("First 5 Rows:")
    st.write(df.head())

    st.write("Shape:", df.shape)

    st.write("Column Data Types:")
    st.write(df.dtypes.astype(str))

    st.write("Missing Values per Column:")
    st.write(df.isnull().sum())

    st.write("Statistical Summary:")
    st.write(df.describe())

    # ---------- Sidebar: column selection ----------
    st.sidebar.title("Attribute Selection")
    col = st.sidebar.selectbox("Select Attribute for Visualization", df.columns)

    # ---------- Bottom section: visualization ----------
    st.write("### Visualization")

    sns.set_style("whitegrid")
    fig, ax = plt.subplots()

    if df[col].dtype == "object":          # categorical column
        st.write("Selected column is Categorical")
        sns.countplot(x=df[col], color="orange", ax=ax)
        ax.set_ylabel("Count")
        ax.set_title("Bar Chart of " + col)
        plt.xticks(rotation=45)
    else:                                  # numerical column
        st.write("Selected column is Numerical")
        sns.histplot(df[col].dropna(), bins=20, kde=True, color="steelblue", ax=ax, edgecolor = "black")
        ax.set_ylabel("Frequency")
        ax.set_title("Histogram of " + col)

    ax.set_xlabel(col)
    st.pyplot(fig)