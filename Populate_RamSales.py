# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:46:40 2020

@author: selam
"""

#import necessary packages
import pyodbc 
import csv
import time
# Create connection to the database
server = '****************'
db = 'Group18HWMart'
username = 'group18' 
password = '********'
conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+username+';PWD='+password
conn = pyodbc.connect(conn_string)
# sql query  to insert rows to to Ram_sales table   
sql_RamSales = '''Insert into Ram_sales(ram_code, time_code, geo_code, 
vendor_code, sales_usd,sales_currency)
values(?,?,?,?,?,?);'''
# function declaration 
def Insert_rows_to_RamSales(RamSalesIfile):
    # Instantiate cursor object
    RamSales_cursor = conn.cursor()
    # control variable for number of rows inserted to Ram_sales table
    ram= 0 
    # open RAM_fact.csv file in read  mode and iterate through rows, parse each row to a list, 
    # cast type of corresponding attribute value, insert the row to Ram_sales table
    with open(RamSalesIfile, "r") as RamSales_file:
        csv_reader = csv.DictReader(RamSales_file)
        start_time = time.time()
        for row in csv_reader:
            # parse row values into list
            row_values = list(row.values())
            ramcode = int(float(row_values[0]))
            timecode = int(row_values[1])
            geocode = int(row_values[2])
            vendorcode = int(row_values[3])
            salesUSD = round(float(row_values[4]),4)
            salescurrency = float(row_values[5])
            RamSales_cursor.execute(sql_RamSales,ramcode,timecode,geocode,
                                    vendorcode,salesUSD,salescurrency)
            ram+=1
            # instantiate row_values list object to empty 
            row_values = []
    elapsed_time = time.time() - start_time 
    # print total number of records written to Gpu_sales table
    print(f" Total number of RAM sales records written to Ram_sales table: {ram} ")
    # print execution time
    print(f" Execution Time: {elapsed_time}")
    # commit insert opearation to the table
    conn.commit()
    conn.close()
# function call
Insert_rows_to_RamSales("F:/LDS/LDS_2020/project_data/RAM_fact.csv")   