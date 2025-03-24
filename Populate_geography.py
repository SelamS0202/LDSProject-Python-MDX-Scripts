# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 20:19:02 2020

@author: UTG 33
"""

import pyodbc 
#import datetime
import csv
#import calendar
server = '****************'
db = 'Group18HWMart'
username = 'group18' 
password = '********'
conn_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+username+';PWD='+password
conn = pyodbc.connect(conn_string)
sql = '''set Identity_insert Geography ON
Insert into Geography(geo_code, continent, country, region, currency)
values(?,?,?,?,?)
set Identity_insert Geography OFF
;'''
my_cursor = conn.cursor()
#list_of_rows = defaultdict(list)
with open("F:/LDS/LDS_2020/project_data/geography.csv", "r") as geography_file:
    csv_reader = csv.DictReader(geography_file)
    i= 0 
    for row in csv_reader:
        row_values = list(row.values())
        geocode = int(row_values[0])
        continent_values = row_values[1]
        country_values = row_values[2]
        region_values = row_values[3]
        currency_values = row_values[4]
        if geocode == 0:
            pass
        else:
            my_cursor.execute(sql,geocode,continent_values,country_values,region_values,currency_values)
            i+=1
        row_values = []
        
print(f" Total number of records written to the table: {i} ")
#my_cursor.close()
conn.commit()
