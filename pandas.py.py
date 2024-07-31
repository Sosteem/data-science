#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandas
"""
import pandas as pd



"""
Series

"""

Age=pd.Series([10,20,30,40],index=['age1','age2','age3','age4']) #adding series
Age.age3 #finding the exceptional value in the index
Filtered_Age=Age[Age>20] #to the the Age and find the value that are greater than 20 and give it back to the filtered_age
Age.values #to print the arrays of the ages
Age.index #to print the index of the age
Age.index=['A1','A2','A3','A4']#CHANGING TH INDEXES
Age.index



"""""""""""
Data frame
"""""""""""

import numpy as np
DF=np.array([[20,10,8],[25,8,10],[27,5,3],[30,9,7]])#using np
Data_set=pd.DataFrame(DF)
Data_set=pd.DataFrame(DF,index=['S1','S2','S3','S4'])
Data_set=pd.DataFrame(DF,index=['S1','S2','S3','S4'],columns=['age','grade1','grade2'])
Data_set['grade3']=[9,6,7,10]
A=Data_set.loc['S2']# loc means location so it means show me the location of S2
Data_set.iloc[1][3] #python starts from 0 and for specific value nikalna
Data_set.iloc[1,3]
Data_set.iloc[:,0]# ':' coloun means all rows
Data_set.iloc[:,2]
Filtered_data=Data_set.iloc[:,1:3]
B=Data_set.drop('grade1',axis=1)
Data_set=Data_set.replace(10,12)
Data_set=Data_set.replace({12:10,9:30})#for creating a dictionary we use {}curly braces //replacing multiple numbers with another numbers
Data_set.head(3)# 3 first rows auacha mostly to check the data in a set
Data_set.tail(2)# last 2 rows 
Data_set.sort_values('grade1',ascending=True)#axis=0 for rows //sorts value in ascending
Data_set.sort_index(axis=0,ascending=True)
Data=pd.read_csv('Data_Set.csv')
