#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"


data = pd.read_csv('UK_monthly_gdp.csv')
print(data)


# In[ ]:




