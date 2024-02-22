#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Monthly data to quarterly data

data['Time Period'] = pd.to_datetime(data['Time Period'],format='/%m/%Y')
data.set_index('Time Period',inplace=True)
quarterly_data = data.resample('Q').mean()
print(quarterly_data.head())

