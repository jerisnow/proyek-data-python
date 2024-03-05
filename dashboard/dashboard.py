import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import urllib

sns.set(style="whitegrid")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load data
customers_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/customers_dataset.csv')
geoloc_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/geolocation_dataset.csv')
order_items = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_items_dataset.csv')
order_pays = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_payments_dataset.csv')
order_review = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/order_reviews_dataset.csv')
orders_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/orders_dataset.csv')
product_category = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/product_category_name_translation.csv')
products_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/products_dataset.csv')
sellers_df = pd.read_csv('D:/Bangkit Academy 2024/Proyek Analisis Data/submission/data/sellers_dataset.csv')

# Title of the dashboard
st.title('E-commerce Dashboard')

# Add a selectbox to the sidebar:
select_option = st.sidebar.selectbox(
    'Select an option:',
    ('Overview', 'Customer Analysis', 'Product Analysis', 'Order Analysis')
)

# Overview page
if select_option == 'Overview':
    st.header('Overview')
    st.write('This page provides an overview of the Brazilian e-commerce dataset.')

# Customer Analysis page
elif select_option == 'Customer Analysis':
    st.header('Customer Analysis')
    st.write('This page provides analysis of customer-related data.')

    # Example visualization
    st.subheader('Customer Distribution by State')
    state_counts = customers_df['customer_state'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=state_counts.index, y=state_counts.values)
    plt.xticks(rotation=45)
    plt.xlabel('State')
    plt.ylabel('Number of Customers')
    st.pyplot()

# Product Analysis page
elif select_option == 'Product Analysis':
    st.header('Product Analysis')
    st.write('This page provides analysis of product-related data.')

    # Example visualization
    st.subheader('Product Categories')
    category_counts = product_category['product_category_name'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values)
    plt.xticks(rotation=90)
    plt.xlabel('Product Category')
    plt.ylabel('Number of Products')
    st.pyplot()

# Order Analysis page
elif select_option == 'Order Analysis':
    st.header('Order Analysis')
    st.write('This page provides analysis of order-related data.')

    # Example visualization
    st.subheader('Order Status')
    order_status_counts = orders_df['order_status'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=order_status_counts.index, y=order_status_counts.values)
    plt.xlabel('Order Status')
    plt.ylabel('Number of Orders')
    st.pyplot()
