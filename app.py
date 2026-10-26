import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="EDA Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Exploratory Data Analysis Interface")

st.sidebar.header("Data Controls")
#file uploader logic
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Failed to read CSV file: {e}")
        st.stop()

    # 3. Dataset Overview
    st.subheader("Dataset Overview")
    st.write("First 5 Rows:")
    st.dataframe(df.head(), use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"Dataset Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
        st.write("Column Data Types:")
        dtypes_df = pd.DataFrame(df.dtypes, columns=["Data Type"]).astype(str)
        st.dataframe(dtypes_df, use_container_width=True)

    with col2:
        st.write("Missing Values per Column:")
        missing_df = pd.DataFrame({
            "Missing Count": df.isnull().sum(),
            "Missing (%)": (df.isnull().sum() / len(df) * 100).round(2)
        })
        st.dataframe(missing_df, use_container_width=True)

    st.write("**Basic Numerical Statistics:**")
    num_cols = df.select_dtypes(include=['number']).columns
    if len(num_cols) > 0:
        stats_df = df[num_cols].describe().T[["mean", "50%", "min", "max"]]
        stats_df.rename(columns={"50%": "median"}, inplace=True)
        st.dataframe(stats_df, use_container_width=True)
    else:
        st.info("No numerical columns found in the dataset.")

    # 4. Attribute Selection
    st.sidebar.markdown("---")
    st.sidebar.header("Attribute Analysis")
    selected_column = st.sidebar.selectbox("Select Attribute for Analysis", df.columns)

    # Detect column type
    if pd.api.types.is_numeric_dtype(df[selected_column]):
        column_type = "Numerical"
    else:
        column_type = "Categorical"

    st.sidebar.info(f"**Detected Type:** {column_type}")

    # 5. Visualization Rendering
    st.markdown("---")
    st.subheader(f"Visualization: {selected_column}")

    fig, ax = plt.subplots(figsize=(9, 4.5))

    if column_type == "Numerical":
        # Histogram with KDE
        sns.histplot(df[selected_column].dropna(), kde=True, ax=ax, color="#bebc0b")
        ax.set_title(f"Value Distribution of '{selected_column}'", fontsize=14, fontweight="bold")
        ax.set_xlabel(selected_column, fontsize=10)
        ax.set_ylabel("Frequency", fontsize=10)
        st.pyplot(fig)
    else:
        # Bar chart for categorical features
        counts = df[selected_column].value_counts(dropna=False)
        bars = ax.bar(counts.index.astype(str), counts.values, color="#1809a0")
        
        ax.set_title(f"Frequency Count of '{selected_column}'", fontsize=14, fontweight="bold")
        ax.set_xlabel(selected_column, fontsize=10)
        ax.set_ylabel("Count", fontsize=10)
        plt.xticks(rotation=45, ha="right")

        # Percentage Display
        total = len(df[selected_column])
        for bar in bars:
            height = bar.get_height()
            percentage = f"{100 * height / total:.1f}%"
            ax.annotate(percentage,
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)

        st.pyplot(fig)

else:
    st.info("Please upload a CSV file via the sidebar to begin EDA.")