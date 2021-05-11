
import pandas as pd 

#loading data set
z = pd.read_csv("C:/Users/hp/Desktop/DataSets/Z_dataset.csv")
 #150*6


#id column is nothing but index 
#droping id columns 
z.drop(z.columns[0], axis = 1, inplace = True) 

z.info()   #For data types and non or null values
# data has no na or nall values 

z.describe() # for mean ,min, max, IQR 

#Graphical Representation
import matplotlib.pyplot as plt
#histogram for square.length
plt.hist(z['square.length']) #histogram

#histogram for 'square.breadth'
plt.hist(z['square.breadth']) #histogram

#histogram for'rec.Length'
plt.hist(z['rec.Length']) #histogram

#histogram for 'rec.breadth'
plt.hist(z['rec.breadth']) #histogram

#histogram for 'colour'
plt.hist(z['colour']) #histogram

# let's find outliers in z
#boxplot for every column
z.columns
boxplot = z.boxplot(column= ['square.length', 'square.breadth', 'rec.Length', 'rec.breadth'])
# square.breadth have some outlier 

# get number of unique values for each column
counts = z.nunique()
counts

#variance for every column
z.var()

#'square.breadth'variance =0.1  
#indicates that all the data values are identical.
#droping square.breadth columns 
z.drop(["square.breadth"], axis = 1, inplace = True) 

