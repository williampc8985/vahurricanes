#!/usr/bin/env python
# coding: utf-8

# In[1]:


# plotting for the USGS river Gage data 


# In[60]:


import matplotlib
import matplotlib.pyplot as plt
from climata.usgs import DailyValueIO
import pandas as pd
import datetime
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
import numpy as np
#Data = np.loadtxt(fname="JamesRiver_DataRequest.txt")
#Data = Data.astype(int)
#print(Data)
Data = ["02016500","02019500","02024750","02024752","02025500","02026000","02029000","02035000","02037500","02037705","02042770","0204289994","02036500"
,"02037000"]
register_matplotlib_converters()
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (20.0, 10.0)


# In[61]:


# set parameters
nyears = 70
ndays = 365 * nyears
for item in Data:
    station_id = item
    param_id = "00060"
    
    datelist = pd.date_range(end=datetime.today(), periods=ndays).tolist()
    data = DailyValueIO(
        start_date=datelist[0],
        end_date=datelist[-1],
        station=station_id,
        parameter=param_id,)
# create lists of date-flow values
    for series in data:
        flow = [r[1] for r in series.data]
        dates = [r[0] for r in series.data]
    
    plt.plot(dates, flow)
    plt.xlabel('Date (yr)')
    plt.ylabel('Streamflow (cfs)')
    plt.title(series.site_name)
    plt.xticks(rotation='vertical')
    plt.show()


# In[50]:





# In[ ]:




