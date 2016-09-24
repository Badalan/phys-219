#Created on July 7, 2016  15:10:33
#@author: Evan and Rob 
############################################################
#
# comments are typcially used to explain the following line of code
#
############################################################

# import the  library numpy  and rename it  np
import numpy as np
# import the library matplotlib   and rename it plot
import matplotlib.pyplot as plt
#name  the input file  with the data
fname = 'NewFile2.csv'

# read in data - the file is assumed to be in csv format (comma separated variables). 
#Files need to be specified with a full path OR they have to be saved in the same folder 
#as the script
data = np.loadtxt(fname, delimiter=',',comments='#' )
# access the data columns and assign variables x and y
#generate  an array  x  which is the first  column  of  data.  Note the first column is 
#indexed as  zero.
x = data[:,0]
#generate  an array  y  which is the second  column  of  data  (index  1)
y = data[:,1]
#note the data is not copied during this process - x,y are 'pointing' to the same 
#memory as data
#define the uncertainty in y. 
sigmay=0.005
# plot the data
plt.errorbar(x, y,yerr=sigmay,marker='o',linestyle='')
## marker='o' : use markers to indicate each data point (x_1,y_1),(x_2,y_2)
## linestyle= '' : no line is drawn to connect the data points
## linestyle= '-' : a line is drawn to connect the data points

# add axis labels
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('This is a title with latex $V(t)=Asin(\omega t)$')
# this next command makes  sure the plot is shown. 
plt.show()
# ----- you can save a figure by right-clicking on the graph in the console
# ----- alternatively use: plt.savefig("NAMEOFFIGURE")