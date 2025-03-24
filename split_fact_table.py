# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:07:13 2020

@author: selam
"""

import csv
global columns
GPU_records = list()
CPU_records = list()
RAM_records = list()
# get list of columns name 
def get_column_name(factFile):
    with open(factFile,"r")as fact_file:
        header_row = ",".join(fact_file.readlines(1))
        columns_names = []
        gpu_col_name = [col  for col in header_row.strip("\n").split(",") if col not in ["Id","cpu_code","ram_code"]]
        cpu_col_name = [col  for col in header_row.strip("\n").split(",") if col not in ["Id","gpu_code","ram_code"]]
        ram_col_name = [col  for col in header_row.strip("\n").split(",") if col not in ["Id","gpu_code","cpu_code"]]
        columns_names.append(gpu_col_name)
        columns_names.append(cpu_col_name)
        columns_names.append(ram_col_name)
        return columns_names
# Split fact file into three files , GPU.csv, CPU.csv,RAM.csv
def split_fact_csv(Input_File,Gpu_outFile,Cpu_outFile, Ram_outFile ):
    g= 0
    c= 0
    r=0
    columns = get_column_name(Input_File)       
    with open (Input_File,"r") as Inputfile:
        fact_reader = csv.DictReader(Inputfile)
        for row in fact_reader:
            gpu = row.get("gpu_code")
            cpu= row.get("cpu_code")
            ram = row.get("ram_code")
            # gpu data
            if ((gpu != "" or gpu == "?") and (cpu == "") and (ram == "")):
                gpu_current_record = {k: v for k, v in row.items() if k not in ["Id", "cpu_code","ram_code"]}
                GPU_records.append(gpu_current_record)
                # cpu data
            elif ((gpu == "") and (cpu != "" or cpu == "?") and (ram == "")):
                cpu_current_record = { kg:vg for kg, vg in row.items() if kg not in ["Id","gpu_code","ram_code"] }
                CPU_records.append(cpu_current_record) 
                # ram data
            else:
                ram_current_record ={kr: vr for kr, vr in row.items()if kr not in ["Id","gpu_code","cpu_code"]}
                RAM_records.append(ram_current_record)
        
    with open(Gpu_outFile,"a",newline= "") as gpu_file:
        # write gpu data into 'GPU.csv'
        csv_writer = csv.DictWriter(gpu_file, fieldnames = columns[0])
        csv_writer.writeheader()
        for gpu_row in GPU_records:
            csv_writer.writerow(gpu_row)
            g+=1
    with open(Cpu_outFile,"a", newline= "") as cpu_file:
        #write cpu data into 'CPU.csv'
        csv_writer2 = csv.DictWriter(cpu_file, fieldnames = columns[1])
        csv_writer2.writeheader()
        for cpu_row in CPU_records:
            csv_writer2.writerow(cpu_row)
            c+=1
    with open(Ram_outFile,"a", newline = "") as ram_file:
        # write ram data into 'RAM.csv'
        csv_writer3 = csv.DictWriter(ram_file, fieldnames = columns[2])
        csv_writer3.writeheader()
        for ram_row in RAM_records:
            csv_writer3.writerow(ram_row)
            r+=1
    print(f"Total number of GPU records: {g}")
    print(f"Total number of CPU records: {c} ")
    print(f"Total number of RAM records: {r}")
            
split_fact_csv("F:/LDS/LDS_2020/project_data/fact.csv","F:/LDS/LDS_2020/project_data/GPU_fact.csv",
               "F:/LDS/LDS_2020/project_data/CPU_fact.csv","F:/LDS/LDS_2020/project_data/RAM_fact.csv")           
        
   

            
    
    
 