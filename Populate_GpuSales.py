# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:16:47 2020

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
# sql query  to insert rows to to Gpu_sales table   
sql_GpuSales = '''Insert into Gpu_sales(gpu_code, time_code, geo_code, 
vendor_code, sales_usd,sales_currency)
values(?,?,?,?,?,?);'''
# function declaration 
def Insert_rows_to_GpuSales(GpuSalesIfile):
    # Instantiate cursor object
    GpuSales_cursor = conn.cursor()
    # control variable for number of rows inserted to Gpu_sales table
    gpu= 0 
    # open GPU_sales.csv file in read  mode and iterate through rows, parse each row to a list, 
    # cast type of corresponding attribute value, insert the row to Gpu_sales table
    with open(GpuSalesIfile, "r") as GpuSales_file:
        csv_reader = csv.DictReader(GpuSales_file)
        start_time = time.time()
        for row in csv_reader:
            # parse row values into list
            row_values = list(row.values())
            gpucode = int(float(row_values[0]))
            timecode = int(row_values[1])
            geocode = int(row_values[2])
            vendorcode = int(row_values[3])
            salesUSD = round(float(row_values[4]),4)
            salescurrency = float(row_values[5])
            GpuSales_cursor.execute(sql_GpuSales,gpucode,timecode,geocode,
                                    vendorcode,salesUSD,salescurrency)
            gpu+=1
            # instantiate row_values list object to empty 
            row_values = []
    elapsed_time = time.time() - start_time 
    # print total number of records written to Gpu_sales table
    print(f" Total number of Gpu sales records written to Gpu_sales table: {gpu} ")
    # print execution time
    print(f" Execution Time: {elapsed_time}")
    # commit insert opearation to the table
    conn.commit()
    conn.close()
    
# function call
Insert_rows_to_GpuSales("F:/LDS/LDS_2020/project_data/GPU_fact.csv")