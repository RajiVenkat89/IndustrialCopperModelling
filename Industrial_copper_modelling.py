import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

st.set_page_config(page_title='INDUSTRIAL COPPER MODELLING',layout="wide")

st.markdown(f'<h1 style= "text-align:center;size:24px;color:blue;">INDUSTRIAL COPPER MODELLING</h1>',unsafe_allow_html=True)
st.header(":blue[**Welcome!!!**]")
df_final=pd.read_csv("https://raw.githubusercontent.com/RajiVenkat89/IndustrialCopperModelling/main/Data/Final%20Data%20for%20Regression%20Model.csv")
with st.sidebar:
    #Option for Prediction of Selling Price/ Status based on User Input
    selected = option_menu(menu_title='PREDICT',options=["SELLING PRICE", "STATUS"], menu_icon="cast", default_index=0)
if (selected=='SELLING PRICE'):
    st.write("Regression Model to identify the Selling Price based on different user parameters")
    #Option for user to enter single set of Input or upload a CSV file containing multiple input set
    tabA,tabB=st.tabs(["SINGLE INPUT","MULTIPLE INPUT"])
    with tabA:
        col1,col2,col3=st.columns(3)
        with col1:
            quantity_tons =st.text_input(label="Quantity (In Tons)", value="", key='text')            
            status=st.selectbox(label="Status",options=df_final["status"].unique(),key="status")
            thickness=st.text_input(label="Thickness",value="",key="thi")
            item_date_day=st.selectbox(label="Item Date Day",options=df_final["item_date_day"].unique(),key="idd")
            delivery_date_day=st.selectbox(label="Delivery Date Day",options=df_final["delivery_date_day"].unique(),key="ddd")
        with col2:
            customer=st.selectbox(label="Customer",options=df_final["customer"].unique(),key="cus")
            item_type=st.selectbox(label="Item Type",options=df_final["item type"].unique(),key="it")            
            width=st.selectbox(label="Width",options=df_final["width"].unique(),key="wid")
            item_date_month=st.selectbox(label="Item Date Month",options=df_final["item_date_month"].unique(),key="idm")
            delivery_date_month=st.selectbox(label="Delivery Date Month",options=df_final["delivery_date_month"].unique(),key="ddm")            
        with col3:
            country=st.selectbox(label="Country",options=df_final["country"].unique(),key="cnt")
            application=st.selectbox(label="Application",options=df_final["application"].unique(),key="app")
            product_ref=st.selectbox(label="Product Reference",options=df_final["product_ref"].unique(),key="prf")            
            item_date_year=st.selectbox(label="Item Date Year",options=df_final["item_date_year"].unique(),key="idy")            
            delivery_date_year=st.selectbox(label="Delivery Date Year",options=df_final["delivery_date_year"].unique(),key="ddy")
        user_input=np.array([[quantity_tons,customer,country,status,item_type,application,thickness,width,product_ref,item_date_day,item_date_month,item_date_year,delivery_date_day,delivery_date_month,delivery_date_year]])
        col4,col5,col6=st.columns(3)
        with col5:
            select=st.button(":blue[**PREDICT SELLING PRICE**]")
            try:
                if select:
                    #Loading the already available pickled Regression Model for Prediction
                    with open('C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Pickle/SellingPrice_Regression.pkl','rb') as fn:
                        sp_model=pickle.load(fn)
                    Sell_Price=sp_model.predict(user_input)
                    st.write(f":green[SELLING PRICE: {round(Sell_Price[0],4)}]")
            except:
                st.write(":red[INVALID INPUT]")
    with tabB:
        upload_file=st.file_uploader("Choose a CSV File",key='reg')
        col1,col2,col3=st.columns(3)
        with col2:
            select=st.button(":blue[CALCULATE SELLING PRICE AND DOWNLOAD]")
            if select:
                try:
                    df_reg=pd.read_csv(upload_file)
                    #Loading the already available pickled Regression Model for Prediction
                    with open('C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Pickle/SellingPrice_Regression.pkl','rb') as fn:
                        sp_model=pickle.load(fn)
                    Sell_Price=sp_model.predict(df_reg)
                    df_reg['Selling Price']=Sell_Price
                    df_reg.to_csv("C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Output/Final Output with Selling Price.csv")
                    st.write(":green[DOWNLOAD COMPLETE]")
                except:
                    st.write(":red[INVALID FILE]")
            
else:
    st.write("Classification Model to identify the Status based on different user parameters")
    #Option for user to enter single set of Input or upload a CSV file containing multiple input set
    tabC,tabD=st.tabs(["SINGLE INPUT","MULTIPLE INPUT"])
    with tabC:
        col1,col2,col3=st.columns(3)
        with col1:
            quantity_tons=st.text_input(label="Quantity (In Tons)", value="", key='qt1')  
            item_type=st.selectbox(label="Item Type",options=df_final["item type"].unique(),key="it1")
            width=st.selectbox(label="Width",options=df_final["width"].unique(),key="wid1")
            item_date_day=st.selectbox(label="Item Date Day",options=df_final["item_date_day"].unique(),key="idd1")
            delivery_date_day=st.selectbox(label="Delivery Date Day",options=df_final["delivery_date_day"].unique(),key="ddd1")
        with col2:
            customer=st.selectbox(label="Customer",options=df_final["customer"].unique(),key="cus1")
            application=st.selectbox(label="Application",options=df_final["application"].unique(),key="app1")
            product_ref=st.selectbox(label="Product Reference",options=df_final["product_ref"].unique(),key="prf1")        
            item_date_month=st.selectbox(label="Item Date Month",options=df_final["item_date_month"].unique(),key="idm1")
            delivery_date_month=st.selectbox(label="Delivery Date Month",options=df_final["delivery_date_month"].unique(),key="ddm1")
        with col3:
            country=st.selectbox(label="Country",options=df_final["country"].unique(),key="cnt1")
            thickness=st.text_input(label="Thickness",value="",key="thi1")
            selling_price=st.text_input(label="Selling Price", value="", key='sp1')            
            item_date_year=st.selectbox(label="Item Date Year",options=df_final["item_date_year"].unique(),key="idy1")      
            delivery_date_year=st.selectbox(label="Delivery Date Year",options=df_final["delivery_date_year"].unique(),key="ddy1")
        user_input_1=np.array([[quantity_tons,customer,country,item_type,application,thickness,width,product_ref,selling_price,item_date_day,item_date_month,item_date_year,delivery_date_day,delivery_date_month,delivery_date_year]])
        col4,col5,col6=st.columns(3)
        with col5:
            select=st.button(":blue[**PREDICT STATUS**]")
            try:
                if select:
                    #Loading the already available pickled Classification Model for Prediction
                    with open('C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Pickle/Status_Classification.pkl','rb') as fn1:
                        st_model=pickle.load(fn1)
                    status=st_model.predict(user_input_1)
                    if(status[0]==7):
                        st.write(f":green[STATUS: SUCCESS]")
                    else:
                        st.write(f":red[STATUS: FAILURE]")
            except:
                st.write(":red[INVALID INPUT]")
    with tabD:
        upload_file=st.file_uploader("Choose a CSV File",key='cls')
        col4,col5,col6=st.columns(3)
        with col5:
            select=st.button(":blue[PREDICT STATUS AND DOWNLOAD FILE]")
            if select:
                try:
                    df_cls=pd.read_csv(upload_file)
                    #Loading the already available pickled Classification Model for Prediction
                    with open('C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Pickle/Status_Classification.pkl','rb') as fn1:
                        st_model=pickle.load(fn1)
                    status=st_model.predict(df_cls)
                    df_cls['Status']=status
                    df_cls['Status']= df_cls['Status'].replace(7,"Success")
                    df_cls['Status']= df_cls['Status'].replace(1,"Failure")
                    df_cls.to_csv("C:/Users/Dharmarajan/Documents/Guvi/Project/Project 4/Output/Final Output with Status.csv")
                    st.write(":green[DOWNLOAD COMPLETE]")
                except Exception as e:
                    st.write(":red[INVALID FILE]")