#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fig = go.Figure(data=go.Heatmap(
z=[data['GDP Growth']],
x=data.index,
y=['GDP Growth'],
colorscale='inferno'))

fig.update_layout(title='GDP Growth over Time',
                 xaxis_title='Time Period',
                 yaxis_title='')
fig.show()

