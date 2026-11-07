#%pip install pandas
#%pip install matplotlib

#importing libraries
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

print("Version of pandas:",pd.__version__)

flights_data = pd.read_csv('flights.csv') 
flights_data.head(10) 
weather_data_pd = pd.read_csv('weather.csv') 
weather_data_np = weather_data_pd.to_numpy()

rowsInFlightData = len(flights_data)
columnsInFlightData = sum(1 for lines in flights_data)

rowsInWeatherData = len(weather_data_pd)
columnsInWeatherData = sum(1 for lines in weather_data_pd)

print("\nFlight data includes",rowsInFlightData,"rows and",columnsInFlightData,"columns.")

print("\nWeather data includes",rowsInWeatherData,"rows and",columnsInWeatherData,"columns.")

#Pandas Data Filtering/Sorting Question Answering 
#use flights_data 

#Question 1 How many flights were there from JFK to SLC? Int
#Question 2 How many airlines fly to SLC? Should be int
#Question 3 What is the average arrival delay for flights to RDU? float
#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
#Question 5 Which date has the largest average depature delay? Pd slice with date and float
    #please make date a column. Preferred format is 2013/1/1 (y/m/d)
#Question 6 Which date has the largest average arrival delay? pd slice with date and float
#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
    #speed = distance/airtime
#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
    #%% Numpy Data Filtering/Sorting Question Answering
    #Use weather_data_np
#Question 9 How many observations were made in Feburary? Int
#Question 10 What was the mean for humidity in February? Float
#Question 11 What was the std for humidity in February? Float

#Question 1 How many flights were there from JFK to SLC? Int
q_1 = int(((flights_data['origin'] == 'JFK') & (flights_data['dest'] == 'SLC')).sum())

print("Number of flights from JFK to SLC:",q_1)

#Question 2 How many airlines fly to SLC? Should be int
q_2 = int(flights_data[flights_data['dest'] == 'SLC']['carrier'].nunique())

print("Number of airlines with SLC as destination:",q_2)

#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = float(flights_data[flights_data['dest'] == 'RDU']['arr_delay'].mean())

print("Average of delay arriving to RDU:",q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
toSea = flights_data[flights_data['dest'] == 'SEA']
fromNyc = toSea['origin'].isin(['LGA', 'JFK']).sum()
q_4 = float(fromNyc / len(toSea)) if len(toSea) > 0 else 0.0

print("Proportion of flights to SEA from the two NYC airports:",q_4)

#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = flights_data['year'].astype(str) + '/' + flights_data['month'].astype(str) + '/' + flights_data['day'].astype(str)
delayByDate = flights_data.groupby('date')['dep_delay'].mean()
maxDepDate = delayByDate.idxmax()
q_5 = pd.Series([delayByDate[maxDepDate]], index=[maxDepDate])

print("Pd slice with the largest average depature delay:\n",q_5)

#Question 6 Which date has the largest average arrival delay? pd slice with date and float
arrDelayByDate = flights_data.groupby('date')['arr_delay'].mean()
maxArrDate = arrDelayByDate.idxmax()
q_6 = pd.Series([arrDelayByDate[maxArrDate]], index=[maxArrDate])

print("Pd slice with the largest average arrival delay:\n",q_6)

#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
nyc2013 = flights_data[flights_data['origin'].isin(['LGA', 'JFK']) & (flights_data['year'] == 2013)].copy()
nyc2013['speed'] = nyc2013['distance'] / nyc2013['air_time']
fastest_flight = nyc2013.loc[nyc2013['speed'].idxmax()]
q_7 = pd.Series([fastest_flight['speed']], index=[fastest_flight['tailnum']])

print("Fastest flight tail number and speed:",q_7)

#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
print("Does the initial file ""weather_data_pd"" contain NaNs?",weather_data_pd.isna().values.any(),"\n")

q_8 = weather_data_pd.fillna(0)

print("Post update, does the q_8 file contain NaNs?",q_8.isna().values.any(),"\n")


#Question 9 How many observations were made in Feburary? Int
columnsList = list(weather_data_pd.columns)
monthIndex = columnsList.index('month')
humidIndex = columnsList.index('humid')

print("Columns in the weather_data_pd\n",columnsList)
print("\nMonth index:",monthIndex,"\nHumid index:",humidIndex)

numFeb = weather_data_np[:, monthIndex] == 2
q_9 = int(np.sum(numFeb))

print("\nNumber of observations in Feb:",q_9)

#Question 10 What was the mean for humidity in February? Float
q_10 = float(np.nanmean(weather_data_np[numFeb, humidIndex].astype(float)))

print("Mean humidity in Feb:",q_10)

#Question 11 What was the std for humidity in February? Float
q_11 = float(np.nanstd(weather_data_np[numFeb, humidIndex].astype(float)))

print("Std humidity in Feb:",q_11)
