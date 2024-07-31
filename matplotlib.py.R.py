"""
visualization with matplotlib

"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

Year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
Temp_I=[0.72,0.61,0.65,0.68,0.75,0.90,1.02,0.93,0.85,0.99,1.02]

plt.plot(Year, Temp_I)
plt.xlabel('Year')
plt.ylabel('Temperature index')
plt.title('Global warming ',{'fontsize':12,'horizontalalignment':'left'})
plt.show() # to render the graph


Month=['Jan','Feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
Customer1=[12,13,9,8,7,8,8,7,6,5,8,10]
Customer2=[14,16,11,7,6,6,7,6,5,8,9,12]
plt.plot(Month,Customer1,color='red',label='Customer1',marker='o')
plt.plot(Month,Customer2,color='black',label='Customer2',marker='2')

plt.ylabel('electricity consumption')
plt.xlabel('Months')
plt.title('Builidng consumption')
plt.legend(loc=1) #for labels to be defined
plt.show()


#for different plots for customer 1
plt.subplot(1,2,1)#row,column,graph number
plt.plot(Month,Customer1,color='red',label='Customer1',marker='o')
plt.xlabel('Months')
plt.title('Builidng consumption of customer 1')
plt.show()

#for different plots for customer 2
plt.subplot(1,2,2)
plt.plot(Month,Customer2,color='black',label='Customer2',marker='2')
plt.xlabel('Months')
plt.title('Builidng consumption of customer 2')
plt.show()


"""
loc for 
location string=location code
'best'=0
'upper right'=1
'upper left'=2
'lower left'=3
'lower right'=4
'right'=5
'center left'=6
'center right'=7
'lower center'=8
'upper center'=9
'center'=10
"""

#scatter plot with grid
plt.scatter(Month,Customer1,color='red',label='Customer1')
plt.scatter(Month,Customer2,color='yellow',label='Customer2')
plt.xlabel('month')
plt.ylabel('Electricity consumption')
plt.title('Scatter plot of building consumption')
plt.grid()
plt.legend(loc='best')
plt.show()


#histogram
plt.hist(Customer1, bins=40,color='pink')
plt.xlabel('Month')
plt.ylabel('Electricity consumption')
plt.title('Histogram')
plt.show()

#bar graph
plt.bar(Month,Customer1,width=0.5,color='Blue')
plt.show()

plt.bar(Month,Customer1,color='red',label='Customer1')
plt.bar(Month,Customer2,color='yellow',label='Customer2')
plt.xlabel('month')
plt.ylabel('Electricity consumption')
plt.title('bar chart')
plt.legend(loc='best')
plt.show()

#two bar graph together
bar_width=0.4
Month_b=np.arange(12)#arrange le 0-11 samma dincha 12 rakhda
plt.bar(Month_b,Customer1,bar_width,color='blue',label='Customer1')
plt.bar(Month_b+bar_width,Customer2,bar_width,color='green',label='customer2')
plt.xlabel('month')
plt.ylabel('Electricity consumption')
plt.title('bar chart')
plt.xticks(Month_b+(bar_width)/12,('Jan','Feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'))#help us to change the labels to 
plt.legend(loc='best')
plt.show()

#box plot (important)
plt.boxplot(Customer1, notch=True, vert= False)#notch gives shapes of notch in box vert is vertical so it gives horizonta;
plt.boxplot([Customer1,Customer2],patch_artist= True,
            boxprops=dict(facecolor='red',color='red'),
            whiskerprops=dict(color='green'),
            capprops=dict(color='blue'),
            medianprops=dict(color='beige'))#patch artist for colors
plt.show()

