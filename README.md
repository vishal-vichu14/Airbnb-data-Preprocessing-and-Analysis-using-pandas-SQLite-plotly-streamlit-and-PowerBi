Airbnb Data Analysis

This project performs data analysis on Airbnb listings using Python, SQLite, Plotly Express, and Streamlit. It involves loading Airbnb data from a CSV file, storing it in an SQLite database, querying the database for insights, and visualizing the results using interactive plots.

Overview

This repository contains scripts and files for:

Data Cleaning and Preparation:

  Loading Airbnb data from a CSV file.
  Selecting relevant columns of interest.
  Handling missing data and cleaning the dataset.
  Saving the cleaned data to a new CSV file.
  Data Analysis and Visualization:

Connecting to SQLite database and loading data.

  Performing SQL queries to retrieve insights such as room type counts, average prices, revenue by room type, etc.
  Using Plotly Express for creating interactive visualizations (pie charts, bar plots) to illustrate the findings.

Streamlit Application:

  Building a Streamlit web application for interactive data exploration.
  Displaying visualizations and insights categorized into different sections:
  Room Type and Revenue
  Room Type and Customers
  Cancellation Policy and Strict Owners
  Property Type

Files

  data_cleaning.py: Python script for cleaning and preparing the Airbnb dataset.
  data_analysis.py: Python script for connecting to SQLite, performing SQL queries, and generating Plotly Express visualizations.
  streamlit_app.py: Streamlit application script for interactive data exploration and visualization.
  Airbnb_data.csv: Cleaned dataset saved after data preparation.

Setup

Install dependencies:

Ensure you have Python installed. Use pip (or pip3 for Python 3) to install the required libraries:

pip install pandas plotly streamlit streamlit_option_menu

Run Streamlit application:

Execute the Streamlit app to launch the web interface locally
streamlit run streamlit_app.py

Explore the data:

Open the Streamlit app in your browser (localhost:8501) to interact with the visualizations and insights.

