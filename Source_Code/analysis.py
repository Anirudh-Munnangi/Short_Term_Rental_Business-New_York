""" This script accepts the two datasets as input and serves as a data quality analysis tool.
It is well documented with comments and readable/user friendly as takes a functional approach.
It contains auxillary functions to generate important charts and visuals which shall be required for analysis.
"""

# Essential library imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import statistics as st
from scipy.stats import mode
plt.style.use('ggplot')
pd.set_option('display.float_format',lambda x:'%.2f'%x)

# Defining Auxillary functions and classes

def replaceNA(x):
	if pd.isnull(x):
		return(-5)
	else:
		return(x)

def predict_revenue_by_dailyprice(data):
	# This function assumes the occupancy to be at 75%
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	revenue_values=[]
	## Prediction by daily price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_daily_prices=(zipcode_filtered_data['price']).tolist()
			yearly_revenue=[0.75*365*float((price[1:]).replace(",","")) for price in list_of_daily_prices]
			median_revenue=st.median(yearly_revenue)
			zipcode_values.append(code)
			revenue_values.append(median_revenue)
	mix=zip(revenue_values,zipcode_values)
	sorted_mix=sorted(mix)
	revenue_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,revenue_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(revenue_values[zipcode_values.index(v)]-2000,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Revenue Per Year')
	plt.title('Median Yearly Revenue Calculated By Daily Price')
	plt.show()


def predict_revenue_by_weeklyprice(data):
	# This function assumes the occupancy to be at 75%
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	revenue_values=[]
	## Prediction by Weekly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_weekly_prices=(zipcode_filtered_data['weekly_price']).tolist()
			yearly_revenue=[0.75*52*float((price[1:]).replace(",","")) for price in list_of_weekly_prices if pd.isnull(price)==False] ## LOT OF NANS ADDRESS IN DATA QUALITY, $ infront ADDRESS IN DATA QUALITY
			if len(yearly_revenue)>=1: # Few zipcodes will be missed out as there are blanks
				median_revenue=st.median(yearly_revenue)
				zipcode_values.append(code)
				revenue_values.append(median_revenue)
	mix=zip(revenue_values,zipcode_values)
	sorted_mix=sorted(mix)
	revenue_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,revenue_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(revenue_values[zipcode_values.index(v)]-2000,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Revenue Per Year')
	plt.title('Median Yearly Revenue Calculated By Weekly Price')
	plt.show()


def predict_revenue_by_monthlyprice(data):
	# This function assumes the occupancy to be at 75%
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	revenue_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_monthly_prices=(zipcode_filtered_data['monthly_price']).tolist()
			yearly_revenue=[0.75*12*float((price[1:]).replace(",","")) for price in list_of_monthly_prices if pd.isnull(price)==False]
			if len(yearly_revenue)>=1:# Few zipcodes will be missed out as there are blanks
				median_revenue=st.median(yearly_revenue)
				zipcode_values.append(code)
				revenue_values.append(median_revenue)
	mix=zip(revenue_values,zipcode_values)
	sorted_mix=sorted(mix)
	revenue_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,revenue_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(revenue_values[zipcode_values.index(v)]-2000,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Revenue Per Year')
	plt.title('Median Yearly Revenue Calculated By Monthly Price')
	plt.show()

def no_of_listings_by_zipcode(data):
	# This function assumes the occupancy to be at 75%
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	listing_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			zipcode_values.append(code)
			listing_values.append(len(zipcode_filtered_data.index))
	mix=zip(listing_values,zipcode_values)
	sorted_mix=sorted(mix)
	listing_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,listing_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(listing_values[zipcode_values.index(v)]+2,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Count of Listings')
	plt.title('Total Number Of Listings by Zipcode')
	plt.show()

def review_score_by_rating(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_rating']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)]+2,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating in Percentage %')
	plt.title('Median Score Ratings By Zipcode')
	plt.show()

def review_score_by_accuracy(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_accuracy']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Accuracy Score Ratings By Zipcode')
	plt.show()

def review_score_by_checkin(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_checkin']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Check-In Score Ratings By Zipcode')
	plt.show()


def review_score_by_cleanliness(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_cleanliness']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Cleanliness Score Ratings By Zipcode')
	plt.show()


def review_score_by_communication(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_communication']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Communication Score Ratings By Zipcode')
	plt.show()

def review_score_by_location(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_location']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Location Score Ratings By Zipcode')
	plt.show()

def review_score_by_value(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	rating_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_ratings=(zipcode_filtered_data['review_scores_value']).tolist()
			list_of_nonnull_ratings=[val for val in list_of_ratings if pd.isnull(val)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if len(list_of_nonnull_ratings)>=1:
				zipcode_values.append(code)
				rating_values.append(st.median(list_of_nonnull_ratings))
	mix=zip(rating_values,zipcode_values)
	sorted_mix=sorted(mix)
	rating_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,rating_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(rating_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Rating on 1 to 10')
	plt.title('Median Value Score Ratings By Zipcode')
	plt.show()


def show_revenue_per_rental(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	revenue_range_lower=[]
	revenue_range_higher=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_minimum_nights=(zipcode_filtered_data['minimum_nights']).tolist()
			list_of_nonnull_minimum_nights=[float(val) for val in list_of_minimum_nights if pd.isnull(val)==False and val<=2*st.median(list_of_minimum_nights)] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			list_of_maximum_nights=(zipcode_filtered_data['maximum_nights']).tolist()
			list_of_nonnull_maximum_nights=[float(val) for val in list_of_maximum_nights if pd.isnull(val)==False and val<=2*st.median(list_of_maximum_nights)] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			list_of_price=(zipcode_filtered_data['price']).tolist()
			list_of_nonnull_price=[float((price[1:]).replace(",","")) for price in list_of_price if pd.isnull(price)==False] # NA RATING VALUES HAVE BEEN REMOVED, Some codes have complete NA values
			if (len(list_of_nonnull_price)>=1 and len(list_of_nonnull_maximum_nights)>=1 and len(list_of_nonnull_minimum_nights)>=1):
				zipcode_values.append(code)
				revenue_range_lower.append((st.median(list_of_nonnull_price))*(st.median(list_of_nonnull_minimum_nights)))
				revenue_range_higher.append((st.median(list_of_nonnull_price))*(st.median(list_of_nonnull_maximum_nights)))
		## Displaying the graphs
		length=len(zipcode_values)
		# Settng the text font dictionary
		font = {'family': 'serif',
        'color':  'black',
        'size': 5,
        }
		# Plotting all lines with text together
		for index in range(0,length):
			xvals=[revenue_range_lower[index],revenue_range_higher[index]]
			yvals=[index+1,index+1]
			plt.text(revenue_range_higher[index]+3000,index+0.5,zipcode_values[index],fontdict=font)
			plt.plot(xvals,yvals)
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Codes')
	plt.xlabel('Max Revenue Expectation')
	plt.title('Revenue Expectation Per Rental')
	plt.show()

def total_hosts_display(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	host_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			list_of_hosts=(zipcode_filtered_data['host_id']).tolist()
			unique_list_of_hosts=set(list_of_hosts)
			if len(unique_list_of_hosts)>=1:# Few zipcodes will be missed out as there are blanks
				zipcode_values.append(code)
				host_values.append(len(unique_list_of_hosts))
	mix=zip(host_values,zipcode_values)
	sorted_mix=sorted(mix)
	host_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,host_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(host_values[zipcode_values.index(v)]+2,i-0.5,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Count Of Hosts')
	plt.title('Counts of Hosts Per Zipcode')
	plt.show()

def HHI_by_count_of_listings(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	hhi_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		hhi_index=0
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			host_values=(zipcode_filtered_data['host_id']).tolist()
			unique_host_values=set(host_values)
			for host in unique_host_values:
				if pd.isnull(host):
					continue
				else:
					market_share_host=(len((zipcode_filtered_data[zipcode_filtered_data['host_id']==host]).index))/(len(zipcode_filtered_data.index))
					hhi_index+=(((market_share_host)*100)**2)
		zipcode_values.append(code)
		hhi_values.append(hhi_index)
	mix=zip(hhi_values,zipcode_values)
	sorted_mix=sorted(mix)
	hhi_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,hhi_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(hhi_values[zipcode_values.index(v)]+2,i-0.5,str(v), color='blue', fontsize="5")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('HHI Index')
	plt.title('Market Concentration By Zipcode: Herfindahl-Hirschman Index')
	plt.show()

def CR_by_count_of_listings(data):
	filtered_data=data[(data['city']=="New York") & (data['bedrooms']==2.0)] # filtered all new york listings
	unique_zip_codes=set(((filtered_data['zipcode']).tolist()))
	zipcode_values=[]
	cr_values=[]
	## Prediction by Monthly price
	for code in unique_zip_codes:
		market_share_list=[]
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=filtered_data[filtered_data['zipcode']==code]
			host_values=(zipcode_filtered_data['host_id']).tolist()
			unique_host_values=set(host_values)
			for host in unique_host_values:
				if pd.isnull(host):
					continue
				else:
					market_share_host=(len((zipcode_filtered_data[zipcode_filtered_data['host_id']==host]).index))/(len(zipcode_filtered_data.index))
					market_share_list.append(market_share_host)
		zipcode_values.append(code)
		# Summing the top 4 market concentration values
		market_share_list.sort(reverse=True)
		crvalue=0
		for index in range(0,len(market_share_list)):
			if index>3:
				break
			else:
				crvalue+=market_share_list[index]
		cr_values.append(crvalue)
	mix=zip(cr_values,zipcode_values)
	sorted_mix=sorted(mix)
	cr_values=[100*val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,cr_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(cr_values[zipcode_values.index(v)],i-0.5,str(v), color='blue', fontsize="5")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Concentration Ratio')
	plt.title('Market Concentration By Zipcode: Concentration Ratio(CR)')
	plt.show()

def time_to_break_even(airbnb_data,zillow_data):
	# Filter for zipcode on zillow data and look for them in the airbnb data after applying city and bedroom filters
	filtered_airbnb_data=airbnb_data[(airbnb_data['city']=="New York") & (airbnb_data['bedrooms']==2.0)] # filtered all new york listings
	filtered_zillow_data=zillow_data[zillow_data['City']=="New York"]
	zip_codes=(filtered_zillow_data['RegionName']).tolist()
	unique_zip_codes=set(zip_codes)
	zipcode_values=[]
	breakeven_values=[]
	# Calculating median time_to_break_even for each zip code
	for code in unique_zip_codes:
		zipcode_filtered_airbnb_data=filtered_airbnb_data[filtered_airbnb_data['zipcode']==str(code)]
		zipcode_filtered_zillow_data=filtered_zillow_data[filtered_zillow_data['RegionName']==code]
		# Check if not empty
		if len(zipcode_filtered_airbnb_data.index)>=1:
			price_of_house=((zipcode_filtered_zillow_data['2017-06']).tolist())[0]
			list_of_daily_prices=(zipcode_filtered_airbnb_data['price']).tolist()
			yearly_revenue=[0.75*365*float((price[1:]).replace(",","")) for price in list_of_daily_prices]
			median_revenue=st.median(yearly_revenue)
			break_even_time=price_of_house/median_revenue
			zipcode_values.append(code)
			breakeven_values.append(break_even_time)
	mix=zip(breakeven_values,zipcode_values)
	sorted_mix=sorted(mix)
	breakeven_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,breakeven_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(breakeven_values[zipcode_values.index(v)],i,str(v), color='blue', fontweight='bold', fontsize="10")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Time In Years')
	plt.title('Median Time To Break Even By Zipcode')
	plt.show()

def appreciation_by_zipcode(data):
	filtered_zillow_data=data[data['City']=="New York"]
	zip_codes=(filtered_zillow_data['RegionName']).tolist()
	unique_zip_codes=set(zip_codes)
	zipcode_values=[]
	appreciation_values=[]
	for code in unique_zip_codes:
		zipcode_filtered_zillow_data=filtered_zillow_data[filtered_zillow_data['RegionName']==code]
		row=zipcode_filtered_zillow_data.iloc[[0]]
		list_of_headers=list(row)
		final_price_value=float(((row['2017-06']).tolist())[0])
		ctr=0
		for index in range(len(list_of_headers)-2,-1,-1):
			value=(((row[list_of_headers[index]]).tolist())[0])
			header=list_of_headers[index]
			if pd.isnull(value) or (header[0:2]!="19" and header[0:2]!="20"):
				break
			else:
				ctr+=1
				start_price_value=float(((row[list_of_headers[index]]).tolist())[0])
		# Calculate the cagr based on first and last values and no of years in terms of ctr/12
		cagr=((final_price_value/start_price_value)**(1/(ctr/12)))-1
		zipcode_values.append(code)
		appreciation_values.append(cagr)
	mix=zip(appreciation_values,zipcode_values)
	sorted_mix=sorted(mix)
	appreciation_values=[100*val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,appreciation_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(appreciation_values[zipcode_values.index(v)],i,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Cagr In Percentage %')
	plt.title('CAGR Of Houses By Zipcode')
	plt.show()

def median_price_of_properties(data):
	filtered_zillow_data=data[data['City']=="New York"]
	zip_codes=(filtered_zillow_data['RegionName']).tolist()
	unique_zip_codes=set(zip_codes)
	zipcode_values=[]
	median_price_values=[]
	for code in unique_zip_codes:
		zipcode_filtered_zillow_data=filtered_zillow_data[filtered_zillow_data['RegionName']==code]
		row=zipcode_filtered_zillow_data.iloc[[0]]
		list_of_headers=list(row)
		price_values=[]
		for index in range(len(list_of_headers)-1,-1,-1):
			value=(((row[list_of_headers[index]]).tolist())[0])
			header=list_of_headers[index]
			if pd.isnull(value) or (header[0:2]!="19" and header[0:2]!="20"):
				break
			else:
				price_values.append(value)
		zipcode_values.append(code)
		median_price_values.append(st.median(price_values))
	mix=zip(median_price_values,zipcode_values)
	sorted_mix=sorted(mix)
	median_price_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,median_price_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(median_price_values[zipcode_values.index(v)],i,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Price Value in $')
	plt.title('Median Price Of Houses By Zipcode')
	plt.show()

def medianprice_vs_sizerank(data):
	filtered_zillow_data=data[data['City']=="New York"]
	zip_codes=(filtered_zillow_data['RegionName']).tolist()
	unique_zip_codes=set(zip_codes)
	size_values=[]
	median_price_values=[]
	for code in unique_zip_codes:
		zipcode_filtered_zillow_data=filtered_zillow_data[filtered_zillow_data['RegionName']==code]
		row=zipcode_filtered_zillow_data.iloc[[0]]
		list_of_headers=list(row)
		price_values=[]
		for index in range(len(list_of_headers)-1,-1,-1):
			value=(((row[list_of_headers[index]]).tolist())[0])
			header=list_of_headers[index]
			if pd.isnull(value) or (header[0:2]!="19" and header[0:2]!="20"):
				break
			else:
				price_values.append(value)
		size_values.append(((row['SizeRank']).tolist())[0])
		median_price_values.append(st.median(price_values))
	plt.scatter(size_values,median_price_values)
	# Setting Graph Propeties
	plt.ylabel('House Price Values in $')
	plt.xlabel('Size Rank value')
	plt.title('House Prices By Size Rank')
	plt.show()

def tourism_insights(airbnb_data,zillow_data):
	tourism_data=pd.read_excel('touristspots.xlsx')
	zipcodes=set((tourism_data['Zipcode']).tolist())
	zipcode_values=[]
	count_values=[]
	for code in zipcodes:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=tourism_data[tourism_data['Zipcode']==code]
			count=len(zipcode_filtered_data.index)
			zipcode_values.append(code)
			count_values.append(count)
	str_zipcode_values=[str(val) for val in zipcode_values]
	mix=zip(count_values,str_zipcode_values)
	sorted_mix=sorted(mix)
	count_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,count_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(count_values[zipcode_values.index(v)],i,str(v), color='blue', fontsize="5")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Count of tourist spots')
	plt.title('Number of Tourist Spots By Zipcode')
	plt.show()

def tourism_insights_intersection(airbnb_data,zillow_data):
	# Getting common zipcodes from both data
	filtered_airbnb_data=airbnb_data[(airbnb_data['city']=="New York") & (airbnb_data['bedrooms']==2.0)] # filtered all new york listings
	filtered_zillow_data=zillow_data[zillow_data['City']=="New York"]
	airbnb_codes=set((filtered_airbnb_data['zipcode']).tolist())
	zillow_codes=set((filtered_zillow_data['RegionName']).tolist())
	str_zillow_codes=[str(val) for val in zillow_codes]
	print(airbnb_codes)
	print("\n\n")
	print(str_zillow_codes)
	zipcode_intesection_values=[val for val in airbnb_codes if val in str_zillow_codes]
	print(zipcode_intesection_values)
	# Filtering tourist data on the common zipcodes
	tourism_data=pd.read_excel('touristspots.xlsx')
	zipcode_values=[]
	count_values=[]
	for code in zipcode_intesection_values:
		if pd.isnull(code):
			continue
		else:
			zipcode_filtered_data=tourism_data[tourism_data['Zipcode']==int(code)]
			count=len(zipcode_filtered_data.index)
			zipcode_values.append(code)
			count_values.append(count)
	str_zipcode_values=[str(val) for val in zipcode_values]
	mix=zip(count_values,str_zipcode_values)
	sorted_mix=sorted(mix)
	count_values=[val[0] for val in sorted_mix]
	zipcode_values=[val[1] for val in sorted_mix]
	y_pos = np.arange(len(zipcode_values))
	plt.barh(y_pos,count_values ,align='center')
	# Attaching labels
	for i, v in enumerate(zipcode_values):
		plt.text(count_values[zipcode_values.index(v)],i,str(v), color='blue', fontweight='bold', fontsize="6")
	# Setting Graph Propeties
	plt.gca().axes.yaxis.set_ticklabels([])
	plt.ylabel('Zip Code Values')
	plt.xlabel('Count of tourist spots')
	plt.title('Number of Tourist Spots By Zipcode')
	plt.show()


def main():
	airbnb_path="/Users/munzi9/Desktop/Python_Scripts/cap/listings.csv"
	zillow_path="/Users/munzi9/Desktop/Python_Scripts/cap/Zip_Zhvi_2bedroom.csv"
	# loading the data
	airbnb_data=pd.read_csv(airbnb_path,low_memory=False)
	zillow_data=pd.read_csv(zillow_path,low_memory=False)

	show_revenue_per_rental(airbnb_data)
	predict_revenue_by_dailyprice(airbnb_data)
	predict_revenue_by_weeklyprice(airbnb_data)
	predict_revenue_by_monthlyprice(airbnb_data)
	no_of_listings_by_zipcode(airbnb_data)
	review_score_by_rating(airbnb_data)
	review_score_by_accuracy(airbnb_data)
	review_score_by_checkin(airbnb_data)
	review_score_by_cleanliness(airbnb_data)
	review_score_by_communication(airbnb_data)
	review_score_by_location(airbnb_data)
	review_score_by_value(airbnb_data)
	total_hosts_display(airbnb_data)
	HHI_by_count_of_listings(airbnb_data)
	time_to_break_even(airbnb_data,zillow_data)
	appreciation_by_zipcode(zillow_data)
	median_price_of_properties(zillow_data)
	medianprice_vs_sizerank(zillow_data)
	CR_by_count_of_listings(airbnb_data)
	tourism_insights(zillow_data,airbnb_data)
	tourism_insights_intersection(airbnb_data,zillow_data)


if __name__=="__main__":
    main()
