""" This script accepts the two datasets as input and serves as a data quality analysis tool.
It is well documented with comments and readable/user friendly as takes a functional approach.
It contains auxillary functions to generate some important charts and visuals which shall be required for analysis.
"""

# Essential library imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Defining Auxillary functions and classes

def replaceNA(x):
	if pd.isnull(x):
		return(-5)
	else:
		return(x)

def analyze_basic_quality(data,header_value):
    # Filtering data based on header value specified and taking the count of values
    filtered_data=data[[header_value]]
    print("Total number of entries= ",len(filtered_data.index),"\n")
    # Getting the list of values in the column
    list_of_values=list((filtered_data[header_value]).values)
    # Getting the unique set of values
    unique_list_of_values=set(list_of_values)
    # Printing number of duplicates
    print("Number of Unique values= ",len(unique_list_of_values),"\n")
    print("No of duplicates= ",len(list_of_values)-len(unique_list_of_values),"\n")
    # check for NAs
    filtered_data['na_values']=filtered_data[header_value].apply(replaceNA)
    na_filtered_data=filtered_data[filtered_data['na_values']==-5]
    print("No of NA values= ",len(na_filtered_data.index),"\n")
    # hidden print statement to see or verify the result
    print(list_of_values)

def analyze_airbnb(data):
    list_of_headers=list(data)
    # Calling the quality check function on each header
    # Attempting to store output in a text file
    sys.stdout=open("quality_analysis_airbnb.txt","w")
    # Running the quality analysis code
    ctr=1
    for val in list_of_headers:
        print("\n\n")
        print("SNo: ",ctr,"\n")
        print("Header Value=",val,"\n")
        analyze_basic_quality(data,val)
        print("\n\n")
        ctr+=1
    # Closing the functionality of priting to a file
    sys.stdout.close()

def analyze_zillow(data):
    list_of_headers=list(data)
    # Calling the quality check function on each header
    # Attempting to store output in a text file
    sys.stdout=open("quality_analysis_zillow.txt","w")
    # Running the quality analysis code
    ctr=1
    for val in list_of_headers:
        print("\n\n")
        print("SNo: ",ctr,"\n")
        print("Header Value=",val,"\n")
        analyze_basic_quality(data,val)
        print("\n\n")
        ctr+=1
    # Closing the functionality of priting to a file
    sys.stdout.close()

def plot_one_column(data,header_value):
	values=(data[header_value]).tolist()
	#new_values=[val for val in values if val<2500]
	plt.plot(new_values)
	#plt.scatter(range(1,len(values)+1),values)
	title_value="Distribution of column: %s<2500"%(header_value)
	plt.title(title_value)
	plt.xlabel("Index of listings")
	plt.ylabel("%s Values"%(header_value))
	plt.show()


def plot_price(data,header_value):
	values=(data[header_value]).tolist()
	price_values=[float((price[1:]).replace(",","")) for price in values if pd.isnull(price)==False]
	plt.plot(price_values)
	title_value="Distribution of column: %s"%(header_value)
	plt.xlabel("Index of listings")
	plt.ylabel("Price Value in $")
	plt.title(title_value)
	plt.show()

def plot_type(data,header_value):
	print(type(((data[header_value]).tolist())[0]))

def main():
	airbnb_path="/Users/munzi9/Desktop/Python_Scripts/cap/listings.csv"
	zillow_path="/Users/munzi9/Desktop/Python_Scripts/cap/Zip_Zhvi_2bedroom.csv"
	# loading the data
	airbnb_data=pd.read_csv(airbnb_path,low_memory=False)
	zillow_data=pd.read_csv(zillow_path,low_memory=False)
	# Analyze Quality of Airbnb data alltogether

	analyze_airbnb(airbnb_data)

	# Analyze Quality of Zillow data alltogether

	analyze_zillow(zillow_data)

	# Analyze individual dataset and column by specifying
	data=airbnb_data # OR zillow_data
	header_value="name" # one of the headers in either of the datasets
	analyze_basic_quality(data,header_value)
	# Plot individual columns
	plot_one_column(airbnb_data,"maximum_nights")# LOTS OF OUTLIERS
	plot_one_column(airbnb_data,"minimum_nights")# LOTS OF OUTLIERS
	plot_one_column(zillow_data,"RegionName")
	plot_price(airbnb_data,"price")# LOTS OF OUTLIERS
	plot_price(airbnb_data,"weekly_price")# LOTS OF OUTLIERS
	plot_price(airbnb_data,"monthly_price")# LOTS OF OUTLIERS
	plot_type(airbnb_data,'square_feet')
	plot_one_column(airbnb_data,'square_feet')
	plot_price(airbnb_data,'security_deposit')


if __name__=="__main__":
    main()
