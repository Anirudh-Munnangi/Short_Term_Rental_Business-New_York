""" This script accepts the two datasets as input and serves as a data munging tool to combine them.
It is well documented with comments and readable/user friendly as takes a functional approach.
It save the filtered input as per our requirements into a json file.
It shows the various timeliness of housing data present per zip code and proposes a function to extract that information.

Functions:
datafile_read(): Reads the files and stores them to class variables

data_filter(): Accepts user filter as a dictionary and filters the data and saves to json file format.
               The filtering process is generic in nature and allows us to explore any kind of market as required.

price_data_view(): Check the zillow price data and prints the amount of monthly price data  available per unique zipcode

zipcode_intersection(): Checks both the datasets and provides the common ones we must take into consideration and move ahead in our analysis.
"""

# Essential library imports
import numpy as np
import pandas as pd
import json
import sys
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Defining Auxillary functions and classes
def perform_filtering(data_file,key,field_value,operation):
    filtered_data=data_file
    if operation=="eq":
        filtered_data=filtered_data[filtered_data[key]==field_value]
    elif operation=="neq":
        filtered_data=filtered_data[filtered_data[key]!=field_value]
    elif operation=="lte":
        filtered_data=filtered_data[filtered_data[key]<=field_value]
    elif operation=="gte":
        filtered_data=filtered_data[filtered_data[key]>=field_value]
    elif operation=="lt":
        filtered_data=filtered_data[filtered_data[key]<field_value]
    elif operation=="gt":
        filtered_data=filtered_data[filtered_data[key]>field_value]
    else:
        print("Wrong operation in filters. Please verify. Thank you.")
        sys.exit()
    return(filtered_data)

class Airbnb_Zillow:

    def __init__(self,path1,path2):
        # Setting the file paths
        self.airbnb_path=path1
        self.zillow_path=path2

    def datafile_read(self):
        # Reading the data files
        self.airbnb_data=pd.read_csv(self.airbnb_path,low_memory=False)
        self.zillow_data=pd.read_csv(self.zillow_path,low_memory=False)

    def data_filter(self,dict_of_filters_airbnb,dict_of_filters_zillow):
        # A function to combine the datafiles as per the filters and save to json
        # Filtering airbnb data
        filtered_data=self.airbnb_data
        for key in dict_of_filters_airbnb.keys():
            values=dict_of_filters_airbnb[key]
            field_value=values[0]
            operation=values[1]
            filtered_data=perform_filtering(filtered_data,key,field_value,operation)
        # Saving to json
        filtered_data.to_json("airbnb_filtered.json")
        # Filtering zillow data
        filtered_data=self.zillow_data
        for key in dict_of_filters_zillow.keys():
            values=dict_of_filters_zillow[key]
            field_value=values[0]
            operation=values[1]
            filtered_data=perform_filtering(filtered_data,key,field_value,operation)
        # Saving to json
        filtered_data.to_json("zillow_filtered.json")


    def price_data_view(self):
        data=self.zillow_data
        filtered_zillow_data=data[data['City']=="New York"]
        zip_codes=(filtered_zillow_data['RegionName']).tolist()
        unique_zip_codes=set(zip_codes)
        zipcode_values=[]
        year_values=[]
        for code in unique_zip_codes:
        	zipcode_filtered_zillow_data=filtered_zillow_data[filtered_zillow_data['RegionName']==code]
        	row=zipcode_filtered_zillow_data.iloc[[0]]
        	list_of_headers=list(row)
        	ctr=0
        	for index in range(len(list_of_headers)-2,-1,-1):
        		value=(((row[list_of_headers[index]]).tolist())[0])
        		header=list_of_headers[index]
        		if pd.isnull(value) or (header[0:2]!="19" and header[0:2]!="20"):
        			break
        		else:
        			ctr+=1
            # Calculate the cagr based on first and last values and no of years in terms of ctr/12
        	zipcode_values.append(code)
        	year_values.append(ctr/12)
        # Sorting the data
        mix=zip(year_values,zipcode_values)
        sorted_mix=sorted(mix)
        year_values=[val[0] for val in sorted_mix]
        zipcode_values=[val[1] for val in sorted_mix]
        # Printing the number of years of house price data present with each zipcode
        for (zipval,yearval) in zip(zipcode_values,year_values):
            print("Zipcode: ",zipval,end="\t")
            print("Years: ",yearval)
        # Ploting graph
        y_pos = np.arange(len(zipcode_values))
        plt.barh(y_pos,year_values ,align='center')
        # Attaching labels
        for i, v in enumerate(zipcode_values):
        	plt.text(year_values[zipcode_values.index(v)],i,str(v), color='blue', fontweight='bold', fontsize="6")
        # Setting Graph Propeties
        plt.gca().axes.yaxis.set_ticklabels([])
        plt.ylabel('Zip Code Values')
        plt.xlabel('Number Of Years')
        plt.title('Years Of House Pricing Data By Zipcode')
        plt.show()

    def zipcode_intersection(self):
        filtered_airbnb_data=self.airbnb_data[(self.airbnb_data['city']=="New York") & (self.airbnb_data['bedrooms']==2.0)] # filtered all new york listings
        filtered_zillow_data=self.zillow_data[self.zillow_data['City']=="New York"]
        airbnb_codes=set((filtered_airbnb_data['zipcode']).tolist())
        zillow_codes=set((filtered_zillow_data['RegionName']).tolist())
        str_zillow_codes=[str(val) for val in zillow_codes]
        zipcode_intesection_values=[val for val in airbnb_codes if val in str_zillow_codes]
        print(zipcode_intesection_values)


def main():
    airbnb_path="/Users/munzi9/Desktop/Python_Scripts/cap/listings.csv"
    zillow_path="/Users/munzi9/Desktop/Python_Scripts/cap/Zip_Zhvi_2bedroom.csv"
    # CREATING an Object of the class which will include basic path information to read the files as input.
    obj=Airbnb_Zillow(airbnb_path,zillow_path)
    obj.datafile_read()
    # Defining dictionaries of filteres for both airbnb and zillow data
    dict_of_filters_airbnb={"city":["New York","eq"],"bedrooms":[2.0,"eq"]}
    dict_of_filters_zillow={"City":["New York","eq"]}
    obj.data_filter(dict_of_filters_airbnb,dict_of_filters_zillow)
    obj.price_data_view()
    obj.zipcode_intersection()


if __name__=="__main__":
    main()
