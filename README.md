# Airbnb Data Analysis

This project performs data analysis on Airbnb listings using Python, SQLite, Plotly Express, and Streamlit. It involves loading Airbnb data from a CSV file, storing it in an SQLite database, querying the database for insights, and visualizing the results using interactive plots.

## Overview

This repository contains scripts and files for:

## Data Cleaning and Preparation:

1. Loading Airbnb data from a CSV file.
2. Selecting relevant columns of interest.
3. Handling missing data and cleaning the dataset.
4. Saving the cleaned data to a new CSV file.

## Data Analysis and Visualization:

## Connecting to SQLite database and loading data.

1. Performing SQL queries to retrieve insights such as room type counts, average prices, revenue by room type, etc.
2. Using Plotly Express for creating interactive visualizations (pie charts, bar plots) to illustrate the findings.

## Streamlit Application:
  
  Building a Streamlit web application for interactive data exploration.

## Displaying visualizations and insights categorized into different sections:

1. Room Type and Revenue
2. Room Type and Customers
3. Cancellation Policy and Strict Owners
4. Property Type

## Files

1. airbnb_data_cleaning.py: Python script for cleaning and preparing the Airbnb dataset.
2. airbnb_analysis.py: Python script for connecting to SQLite, performing SQL queries, and generating Plotly Express visualizations.
3. airbnb_project_report.pbit:  Power BI template file (.pbit) designed for generating comprehensive project reports based on Airbnb data analysis.
4. airbnb_project_report.pdf: This PDF document serves as a detailed report summarizing findings from the Airbnb data analysis project.
  
## Setup

## Install dependencies:

  Ensure you have Python installed. Use pip (or pip3 for Python 3) to install the required libraries:

  pip install pandas plotly streamlit streamlit_option_menu

## Run Streamlit application:

Execute the Streamlit app to launch the web interface locally

streamlit run streamlit_app.py

## Explore the data:

Open the Streamlit app in your browser (localhost:8501) to interact with the visualizations and insights.

