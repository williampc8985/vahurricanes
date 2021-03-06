#!/usr/bin/env python
# coding: utf-8

#loading modules/libraries
import numpy
import matplotlib
import decimal
#loading .csv from GIS
numpy.loadtxt(fname= "simplecoast.csv", delimiter = ",")
#importing the csv that I created from a GIS shapefile trace & transforming into a re-useable variable
coastline = (numpy.loadtxt(fname = "simplecoast.csv",delimiter = ","))
#examining the data
print(coastline)
print (type(coastline))
print(coastline.dtype)
print(coastline.shape)
# need to separate the data by x and y so that I can plot it.
# x-data
x = coastline[:,0]
#y-data
y = coastline[:,1]
#print(x)
#print(y)
matplotlib.pyplot.plot(x,y)
# the simple coastline is created for the MD,VA and NC coastal borders. 

