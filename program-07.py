#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:40:13 2020

@author: lheusing
create a series of plots from data csv. without using genfromtxt
create hist, KDE, latvslong, cd plot, scatter, Q-Q plot of the data
see metadata on data source and plot descriptors
"""


import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
import scipy


data = pn.read_table( 'all_month.csv',sep = ',')


#clean mag data from NAN
mag = data['mag'].dropna()


#histogram plot
plt.hist(mag, bins=10,range = (0,10))
plt.xlabel('magnitude')
plt.savefig('magnitude hist.jpeg')
plt.close()

#kde plot scotts
mag.plot.kde()
plt.savefig('magnitude kde.jpeg')
plt.close()

#lat long plot 
plt.plot(data['longitude'],data['latitude'],'g^' )
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('lat long scatter.jpeg')
plt.close()

#CD plot normalized
depth = data['depth'].dropna()
depth = np.sort(depth)
norm = np.linspace(0,1,len(depth)) #normalize data
plt.plot(depth,norm)
plt.xlabel('depth')
plt.savefig('depth cd.jpeg')
plt.close()

#mag vs depth plot
mag2 = data['mag'].fillna(1) #replace na with 1 to match size of depth array and wont distrub figure

plt.scatter(mag2 ,depth)
plt.xlabel('magnitude')
plt.ylabel('depth')
plt.savefig('mag vs depth.jpeg')
plt.close()

#qq plot
scipy.stats.probplot(mag, plot = plt)
plt.ylabel('magnitude')
plt.savefig('Q-Q magnitude.jpeg')
plt.close()
