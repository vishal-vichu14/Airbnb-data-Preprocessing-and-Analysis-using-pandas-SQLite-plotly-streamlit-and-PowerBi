import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

# Load data from CSV into SQLite table
data = pd.read_csv("C:/Users/visha/Downloads/Airbnb_data.csv")
data.to_sql("air", conn, if_exists='replace', index=False)

# SQL queries
roomtype_vs_count=pd.read_sql_query(''' SELECT room_type,COUNT(*) from air GROUP BY room_type ''',conn)
roomtype_vs_price=pd.read_sql_query('''SELECT room_type,avg(price) from air GROUP BY room_type ORDER BY avg(price)''',conn)
roomtype_vs_sumprice=pd.read_sql_query('''SELECT room_type,sum(price) from air GROUP BY room_type''',conn)
roomtype_vs_accommodate=pd.read_sql_query('''SELECT room_type,avg(accommodates) from air GROUP BY room_type''',conn)
roomtype_vs_bedroom=pd.read_sql_query('''SELECT room_type,avg(bedrooms) from air GROUP BY room_type''',conn)
roomtype_vs_beds=pd.read_sql_query('''SELECT room_type,avg(beds) from air GROUP BY room_type''',conn)
protype_vs_count=pd.read_sql_query('''SELECT property_type,COUNT(*) from air GROUP BY property_type ORDER BY COUNT(*) desc''',conn)
protype_vs_pricesavg=pd.read_sql_query('''SELECT property_type,avg(price) from air GROUP BY property_type ORDER BY avg(price) desc''',conn)
protype_vs_pricesum=pd.read_sql_query('''SELECT property_type,sum(price) from air GROUP BY property_type ORDER BY sum(price) desc''',conn)
cancle_vs_price=pd.read_sql_query('''SELECT cancellation_policy,avg(price) from air GROUP BY cancellation_policy''',conn)
cancle_vs_count=pd.read_sql_query('''SELECT cancellation_policy,COUNT(*) from air GROUP BY cancellation_policy''',conn)
cancle_vs_epeople=pd.read_sql_query('''SELECT cancellation_policy,avg(extra_people) from air GROUP BY cancellation_policy''',conn)
cancle_vs_pricesum=pd.read_sql_query('''SELECT cancellation_policy,sum(price) from air GROUP BY cancellation_policy''',conn)
customer= pd.merge(roomtype_vs_accommodate, roomtype_vs_bedroom, on='room_type')
customers=pd.merge(customer,roomtype_vs_beds,on='room_type')

# Merge data for visualization
customer = pd.merge(roomtype_vs_accommodate, roomtype_vs_bedroom, on='room_type')
customers = pd.merge(customer, roomtype_vs_beds, on='room_type')

# Visualizations using Plotly Express
roomtype_vs_count_fig=px.pie(roomtype_vs_count,names='room_type',values='COUNT(*)',title='Room type Count')
roomtype_vs_price_fig=px.bar(roomtype_vs_price,x='room_type',y='avg(price)',color='room_type',title='Room type vs AVG.price')
roomtype_vs_sumprice_fig=px.pie(roomtype_vs_sumprice,names='room_type',values='sum(price)',title='Room type vs Revenue')
protype_vs_count_fig=px.bar(protype_vs_count,x='property_type',y='COUNT(*)',color='property_type',title='Property type Count')
protype_vs_pricesavg_fig=px.bar(protype_vs_pricesavg,x='property_type',y='avg(price)',color='property_type',title='Property type vs AVG.price')
protype_vs_pricesum_fig=px.bar(protype_vs_pricesum,x='property_type',y='sum(price)',color='property_type',title='Property type vs Revenue')
cancle_vs_price_fig=px.bar(cancle_vs_price,x='cancellation_policy',y='avg(price)',color='cancellation_policy',title='cancellation policy vs Price')
cancle_vs_count_fig=px.bar(cancle_vs_count,x='cancellation_policy',y='COUNT(*)',color='cancellation_policy',title='cancellation policy Count')
cancle_vs_epeople_fig=px.bar(cancle_vs_epeople,x='cancellation_policy',y='avg(extra_people)',color='cancellation_policy',title='cancellation policy vs extra people')
cancle_vs_pricesum_fig=px.pie(cancle_vs_pricesum,names='cancellation_policy',values='sum(price)',title='cancellation policy vs Revenue')

# Plots for Room Type and Customers
df_entire_home = customers[customers['room_type'] == 'Entire home/apt']
fig_entire_home = px.bar(df_entire_home,
                         x='room_type',
                         y=['avg(accommodates)', 'avg(bedrooms)', 'avg(beds)'],
                         barmode='group',
                         labels={'value': 'Average Count', 'variable': 'Metric'},
                         title='Average Accommodates, Bedrooms, and Beds - Entire home/apt'
                         )
df_private_room = customers[customers['room_type'] == 'Private room']
fig_private_room = px.bar(df_private_room,
                          x='room_type',
                          y=['avg(accommodates)', 'avg(bedrooms)', 'avg(beds)'],
                          barmode='group',
                          labels={'value': 'Average Count', 'variable': 'Metric'},
                          title='Average Accommodates, Bedrooms, and Beds - Private room'
                          )
df_shared_room = customers[customers['room_type'] == 'Shared room']
fig_shared_room = px.bar(df_shared_room,
                         x='room_type',
                         y=['avg(accommodates)', 'avg(bedrooms)', 'avg(beds)'],
                         barmode='group',
                         labels={'value': 'Average Count', 'variable': 'Metric'},
                         title='Average Accommodates, Bedrooms, and Beds - Shared room'
                         )

# Streamlit application
image_path = "C:/Users/visha/Downloads/Airbnb_logo_PNG3.png"
st.image(image_path, use_column_width=True)

# Main title
st.markdown('<h1 style="color: pink;">Airbnb Analysis</h1>', unsafe_allow_html=True)

# Sidebar with options
with st.sidebar:
    image2_path = "C:/Users/visha/Downloads/Airbnb_logo_PNG8.png"
    st.image(image2_path, use_column_width=True)
    selected = option_menu("Main Menu", ["HOME", 'Analysis'],
                           icons=['house', 'graph-up'], menu_icon="cast", default_index=0)

# Analysis section
if selected == "Analysis":
    # Room Type and Revenue section
    with st.expander("Room Type and Revenue"):
        st.write(roomtype_vs_count_fig)
        st.write('Number of properties with Entire home/apartment is higher.')
        st.write(roomtype_vs_sumprice_fig)
        st.write('Properties with Entire home/apartment generate higher revenue.')
        st.write(roomtype_vs_price_fig)
        st.write('However, the average price of Shared room is higher.')
        st.write('Increasing the number of Shared rooms or converting Entire home/apartment into Shared rooms can generate more revenue.')

    # Room Type and Customers section
    with st.expander("Room Type and Customers"):
        st.write(fig_entire_home)
        st.write('People accommodated: 4-5 people')
        st.write('Number of bedrooms: 1-2 bedrooms')
        st.write('Number of beds: 2-3 beds')
        st.write("Suitable for families")

        st.write(fig_private_room)
        st.write('People accommodated: 2-3 people')
        st.write('Number of bedrooms: 1 bedroom')
        st.write('Number of beds: 1-2 beds')
        st.write("Suitable for couples")

        st.write(fig_shared_room)
        st.write('People accommodated: 3-4 people')
        st.write('Number of bedrooms: 1 bedroom')
        st.write('Number of beds: 2-3 beds')
        st.write("Suitable for working people and students")

    # Cancellation Policy and Strict Owners section
    with st.expander("Cancellation Policy and Strict Owners"):
        st.write(cancle_vs_count_fig)
        st.write('Most properties have a strict 14-day grace period.')
        st.write(cancle_vs_price_fig)
        st.write('Properties with strict owners charge higher prices.')
        st.write(cancle_vs_epeople_fig)
        st.write('Strict owners allow fewer extra people in their properties.')
        st.write(cancle_vs_pricesum_fig)
        st.write('People prefer less strict owners, and many owners offer a strict 14-day grace period, resulting in higher revenue.')

    # Property Type section
    with st.expander("Property Type"):
        st.write(protype_vs_count_fig)
        st.write('Most properties are apartments.')
        st.write(protype_vs_pricesavg_fig)
        st.write('Properties like Boat houses and Heritage Hotels have high average prices.')
        st.write(protype_vs_pricesum_fig)
        st.write('Apartments generate higher revenue.')
