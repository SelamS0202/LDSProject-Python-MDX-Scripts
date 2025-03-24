Developed for Labratory of Data Science Course project:
The Python scripts were developed to extract data from given CSV files (sales data for three product lines: GPU, CPU, and RAM; geography data; sales period data; and vendor data) and 
ingest it into the respective tables to build a data warehouse based on a fact constellation schema. 
The dimensions include Time, Geography, Vendor, and Product.

The MDX file answers the following questions from an OLAP cube built for multi diemsional anlysis based on the data warehouse: The percentage increase in total sales with respect to the previous month for each RAM
 brand and each country, For each region and RAM brand show the total sales in percentage with respect to the total
 sales of the corresponding country, RAM memory types having a total sales greater than 10 percent of the totals sales in
 each continent by continent and year
