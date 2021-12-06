#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import ephem
import os
import time


# In[54]:


os.environ['TZ'] ='Nepal'# 'US/Pacific$'
time.tzset()
print("Time zone calibrated to", os.environ['TZ'])
def get_full_moons_in_year(StYear, EndYear, mm, day):
    """
    Generate a list of full moons/ Purnimas  for a given date  calibrated to the local time zone
    :StYear year: Starting date year
    : EndYear= up untill which year
    : mm= month
    : day= Day
    :return: list of dates as strings in the format YYYY-mm-dd
    # Author: Abhi 
    # Reference: 
    https://www.py4u.net/discuss/145808
"""
    moons = []
    date = ephem.Date(datetime.date(StYear, mm, day))
    end_date = ephem.Date(datetime.date(EndYear, mm, day))
    while date <= end_date:
        date = ephem.next_full_moon(date)
        # Convert the moon dates to the local time zone, 
        local_date = ephem.localtime(date)
        if date<end_date:
            # Append the date 
            moons.append(local_date.strftime("%Y-%m-%d"))

    return moons


# In[60]:


### Number of Purnima Calculation  

res=[];c=0
birthYear=1940
CurrentYear=2021
month=12;day=3
moons = get_full_moons_in_year(birthYear,CurrentYear, month, day )

print('Number of Purnimas between 1940 Dec 3 and 2021 Dec 3 are {}'.format(len(moons)))
print('List of All Purnimas are as below')
print ("First Purnima Date ={}, Last Purnima Date {}".format(moons[0], moons[-1]))


# In[ ]:




