# First, import the relevant modules
import requests
import json
import re


# -------------------------- Sorting Functions(Merge Sort) --------------------------
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


# ------------------------- Function to find median in a sorted list --------------------------
def median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 0:
        median1 = sorted_list[n//2] 
        median2 = sorted_list[n//2 - 1] 
        median = (median1 + median2)/2
    else:
        median = sorted_list[n//2]
    
    return median


API_KEY = '5_dcLN33pY-Rswbv9WLq'

# Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
BASE_URL = f'https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date=2017-01-01&end_date=2017-12-31api_key={API_KEY}'
apiResponse = requests.get(url=BASE_URL)




if(apiResponse.ok):
    # Convert the returned JSON object into a Python dictionary.
    data_dict = json.loads(apiResponse.content.decode('utf-8'))
    
    print("--------------------- response recieved ---------------------")
    
    highestOpening = 0
    lowestOpening = 9999999
    largestChange = 0
    sum = 0
    unsortedTradingVolumeArray = []

    # print('----------------- DATA TYPE -----------------')
    # print(data_dict['dataset']['column_names'])
    
    
    
    # -------- Calculate what the highest and lowest opening prices were for the stock in this period.
    # -------- What was the largest change in any one day (based on High and Low price)?
    # -------- What was the largest change between any two days (based on Closing Price)?
    # -------- What was the average daily trading volume during this year?
    # -------- (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)
    for eachElement in data_dict['dataset']['data']:
        change = eachElement[2] - eachElement[3]
        change = round(change,2)
        sum = sum + eachElement[6]
        unsortedTradingVolumeArray.append(eachElement[6])
        
        # print('------------------------------- In Loop -------------------------------')
        # print(eachElement)
        # print('current open price:', eachElement[1])
        # print('current opening high:', highestOpening)
        # print('current opening low:', lowestOpening)
        # print('current daily change:', change)
        # print('largest daily change:', largestChange)

        # Check if the element is not null
        if eachElement[1]:
            if eachElement[1] > highestOpening:
                highestOpening = eachElement[1]
            if eachElement[1] < lowestOpening:
                lowestOpening = eachElement[1]
            if change > largestChange:
                largestChange = change

    
    
    averageDailyTradingVolume = sum / len(data_dict['dataset']['data'])
    sortedDailyTradingVolume = merge_sort(unsortedTradingVolumeArray)
    medianDailyTradingVolume = median(sortedDailyTradingVolume)
    print('-------------------------------------------------------------- Out of loop --------------------------------------------------------------')
    print('total entries:', len(sortedDailyTradingVolume))
    print('Highest Opening price in period:', highestOpening)
    print('Lowest opening price in period:', lowestOpening)
    print('largest change in one day:', largestChange)
    print('average daily trading volume:', averageDailyTradingVolume)
    print('median daily trading volume:', medianDailyTradingVolume)
    
else:
    print("ERROR in response")
    print(apiResponse)




# ------------------------------------------------------------- API Usage Notes -------------------------------------------------------------
# https://www.quandl.com/data/FSE-Frankfurt-Stock-Exchange
# https://www.quandl.com/api/v3/datasets/EOD/AAPL?start_date=2016-01-01&end_date=2016-01-31&api_key=YOURAPIKEY
# https://www.quandl.com/api/v3/datasets/WIKI/FB/data.csv?column_index=4&exclude_column_names=true&rows=3&start_date=2012-11-01&end_date=2013-11-30&order=asc&collapse=quarterly&transform=rdiff



# ----------------------------------------------------------- Project Description -----------------------------------------------------------
# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# # Store the API key as a string - according to PEP8, constants are always named in all upper case
# API_KEY = ''
# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are 
# also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. 
# We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, 
# as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the requests package, 
# which can be easily downloaded using pip or conda. You can find the documentation for the package here: http://docs.python-requests.org/en/master/

# Finally, apart from the requests package, you are encouraged to not use any third party Python packages, such as pandas, and instead focus
# on what's available in the Python Standard Library (the collections module might come in handy: https://pymotw.com/3/collections/). 
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, 
# though some questions can also be answered using lists. You can read more on these
# data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. 
# Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# # First, import the relevant modules
# # Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# # into the JSON structure that will be returned
# # Inspect the JSON structure of the object you created, and take note of how nested it is,
# # as well as the overall structure
# These are your tasks for this mini project:

# Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# Convert the returned JSON object into a Python dictionary.
# Calculate what the highest and lowest opening prices were for the stock in this period.
# What was the largest change in any one day (based on High and Low price)?
# What was the largest change between any two days (based on Closing Price)?
# What was the average daily trading volume during this year?
# (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)
# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure


