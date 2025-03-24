# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:21:05 2020

@author: selam
"""
import pyodbc
import csv
#server = 'tcp:apa.di.unipi.it'
#db = 'Group18HWMart'
#username = 'group18' 
#password = 'o3voh'
#conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+username+';PWD='+password
#conn = pyodbc.connect(conn_string)
#vendor_cursor = conn.cursor()
sql = "insert into vendor(vendor_code,name) values(?,?);"
def create_connection(server, db, username,password):
    conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+username+';PWD='+password
    conn = pyodbc.connect(conn_string)
    return conn.cursor()
# read vendor.csv file and insert records to vendor 
def read_and_populate_vedor_table(Input_file, query):
    vendor_cursor = create_connection('tcp:apa.di.unipi.it', 'Group18HWMart','group18','o3voh')
    
    
    
