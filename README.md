# MapReduce

Q1).  A log file (purchase,csv) is extracted from the database of a retailer. It contains the following tab-delimited fields:

date of purchase
time of purchase
store name
product type
cost
method of payment

Preview of the log file follow
 

I.	Down load the dataset (purchase,csv) from courseweb
II.	Create a folder in HDFS called /user/test/input
III.	Move the dataset from local to HDFS (/user/test/input

Write MapReduce codes in python to answer the following questions. Execute the python codes and capture the results:
a.	Total and average sales per product type
b.	Total and average sales for method of payment.
c.	Highest and lowest individual sale for each store
d.	Total sales value across all stores and average number of sales
e.	Mean of sales for each month

Q2).
The sample dataset contains the petrol distribution details and dataset can be downloaded at https://drive.google.com/open?id=0B1QaXx7tpw3SMTBqLUQwX0lOWnM. The preview of the dataset is given below.
 
I.	Down load the dataset in one of the following ways
a.	Download directly to VM using wget
b.	Go to the URL and manually download the dataset to the linked folder.
II.	Move the dataset from local to HDFS  (/user/test/input)
Write the Hive commands and execute in order to do the following tasks.
a.	Create a hive table and load the dataset.
b.	What is the total amount of petrol in volume sold by every distributor
c.	Which are the top 10 distributors ID’s for selling petrol and also display the amount of petrol sold in volume by them individually?
d.	Find real life 10 distributor name who sold petrol in the least amount.

Q3).
Dataset about Walmart Stock from the years 2012-2017 is available in courseweb (Walmart.csv)
a.	Download the above dataset file and store it in your VM
Answer the following question by writing the code either in Scala or Python and execute them in spark-shell or pyspark accordingly.
a.	Load the Walmart Stock data file into a DataFrame, have Spark infer the data types.
b.	User describe() to learn about the DataFrame
c.	Print the first five rows.
d.	There are too many decimal places for most of the fields in the describe() dataframe. Format the numbers to just show up to two decimal places. Pay careful attention to the datatypes that .describe() returns.
e.	Create a new dataframe with a column called HV Ratio that is the ratio of the High Price versus volume of stock traded for a day.
f.	What day had the Peak High in Price?
g.	What is the mean of the Close column?
h.	What is the max and min of the Volume column?
i.	How many days was the Close lower than 60 dollars?
j.	What percentage of the time was the High greater than 80 dollars? In other words, (Number of Days High>80)/(Total Days in the dataset)
k.	What is the max High per year?
l.	What is the average Close for each Calendar Month? In other words, across all the years, what is the average Close price for Jan, Feb, Mar, etc. Your result will have a value for each of these months.
