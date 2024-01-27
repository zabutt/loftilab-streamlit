import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Lofti Lab - Playground")

    st.header("Upload your CSV data file")
    data_file = st.file_uploader("Upload CSV", type=["csv"])

    if data_file is not None:
        data = pd.read_csv(data_file)
        st.write("Data overview:")
        st.write(data.head())

        st.sidebar.header("Visualizations")
        plot_options = ["Bar plot", "Scatter plot", "Histogram", "Box plot"]
        selected_plot = st.sidebar.selectbox("Choose a plot type", plot_options)

        

if __name__ == "__main__":
    main()