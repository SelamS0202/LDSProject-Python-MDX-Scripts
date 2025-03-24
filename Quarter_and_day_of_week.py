# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:54:24 2020

@author: selam
"""
import csv
import math
import datetime
import calendar
def write_header(Input_filename, Output_filename):
# read input file, time.csv and fetch and update colums name list
# Write the updated colums name list into the output file, time_updated.csv
    with open(Input_filename, "r") as hfile:
        attributes = ''.join(hfile.readlines(1))
        attributes_list = [colum for colum in attributes.strip("\n").split(",")]
        attributes_list.extend(["quarter","day_of_week"])
    with open(Output_filename, "a",newline = "") as outhfile2:
        csv_header_writer = csv.DictWriter(outhfile2,fieldnames= attributes_list)
        csv_header_writer.writeheader()

# open the input file , time.csv and drive the 'quarter' and 'day_of_week' columns
# from year, month and day columns   
def update_timecsv_columns(Inputfname, Outputfname):
    # call write_header function to write the header into the output file, time_updated.csv
    write_header(Inputfname, Outputfname)
    with open(Inputfname, "r") as rfile:
        current_row = []
        csv_reader = csv.DictReader(rfile)
        for row in csv_reader:
            YMD = str(row['year']+ row['month'] + row['day'])
            YMD_date = datetime.datetime.strptime(YMD, "%Y%m%d").date()
            quarter_var = str("Q") + str(math.ceil(YMD_date.month/3))
            week_name = YMD_date.weekday()
            day_of_week_var = calendar.day_name[week_name]
            current_row.append(quarter_var)
            current_row.append(day_of_week_var)
            # update the each row with the new values, quarter and day_of_week columns
            # and write to the output file, time_test2
            with open(Outputfname, "a",newline="") as wfile:
                csv_writer = csv.DictWriter(wfile, row.keys())
                row.update({'quarter': current_row[0], 'day_of_week': current_row[1]})
                csv_writer.writerow(row)
            current_row = []
# finally, call the function 
update_timecsv_columns("C:/Users/selam/Desktop/Assignment_1/time.csv",
                       "C:/Users/selam/Desktop/Assignment_1/time_updated.csv")


