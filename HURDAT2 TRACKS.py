#!/usr/bin/env python
# coding: utf-8

# In[1]:


# we want storm number, name, class and location for each path.


# In[2]:


# the first thing is to import pandas and datatime
import pandas as pd
import datetime
from datetime import datetime


# In[3]:


# we know that the lat long is north-west, turn them into floating pt values
def lat_lon_to_float(v):
    """
    convert strings from HNC to float locations
    
    """
#the following is the test for conversion of lat long     
    if(v[-1] =="S") or (v[-1] == "W"):
        multiplier = -1
    else:
        multiplier = 1
    return float(v[:-1])* multiplier
# so if there is an S or W it gets a negative in front


# In[30]:


#now we have to read the data (text) into the machine
#1. create an empty list to hold the data that we want
data = []

#open the data in "r", read mode...with file handle f
# remember: .strip() removes the white space in the text. 

with open("hurdat2.txt","r") as f:
    for line in f.readlines():
        if line.startswith("AL"):
            storm_id = line.split(",")
            storm_number = storm_id[0].strip()
            storm_name = storm_id[1].strip()
        else:
            location_line = line.split(",")
            dt = datetime.strptime(location_line[0] + location_line[1], "%Y%m%d %H%M")
            storm_status = location_line[3].strip()
            #each of the lines below is a column in the table.
            storm_lat = lat_lon_to_float(location_line[4].strip())
            storm_lon = lat_lon_to_float(location_line[5].strip())
            max_speed = lat_lon_to_float(location_line[6].strip())
            #now after parsing we can append them to our data list
            data.append([storm_number, storm_name, storm_status, storm_lat, storm_lon, dt, max_speed])


# In[31]:


data[0]


# In[32]:


# now make the dataframe
df = pd.DataFrame(data,columns=["Storm Number","Storm Name", "Storm Status", "Lat", "Lon", "Time", "Max Speed"])


# In[33]:


#test the table
df.head()


# In[8]:


#how many storms have unique lengths?
len(df["Storm Number"].unique())


# In[9]:


# what about how many lines have different storm status?
#here is a table of the different designations, as shown in the .pdf that came with HURDAT
df.groupby("Storm Status").count()


# In[10]:


conda install -c conda-forge cartopy


# In[11]:


# now we need to plot this on the map that was previously created.
# this is where matplotlib will come in
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
#MAGIC  - render the figure in the notebook.
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


# set coordinate ref. systems
plot_crs =ccrs.LambertConformal(central_longitude = -100., central_latitude = 45)
data_crs =ccrs.PlateCarree()
#figures
fig = plt.figure(figsize = (6,6))

#axis
ax = plt.subplot(1,1,1, projection=plot_crs)
ax.set_extent([-78, -72, 33, 39], data_crs)

#background map
ax.coastlines("50m", edgecolor = "k", linewidth = 0.75)
ax.add_feature(cfeature.STATES, linewidth = 0.5)

###Just the Hurricanes - this can bbe changed for the designation that is desired, see the .pdf for more choices.
df_hu = df[df["Storm Status"]=="HU"]

###Time period - from 2020-the time length of interest - Ex: 2020-100 = 100 years of data 
df_hu = df_hu[df_hu["Time"]> datetime(2020-30,1,1)]


#plotting loop for every unique storm
for storm_number in df_hu["Storm Number"].unique():
    storm_data = df_hu[df_hu["Storm Number"]==storm_number]
    ax.plot(storm_data["Lon"], storm_data["Lat"], transform=data_crs)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




