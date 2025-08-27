import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# LINEPLOT
# x=np.linspace(0,10,100)
# y=np.sin(x)
# plt.plot(x,y,color='blue',linestyle='--',marker='o')
# plt.title("line plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()


# SCATTER PLOT
# x=np.random.rand(50)
# y=np.random.rand(50)
# plt.scatter(x,y,color="blue",marker="*")
# plt.title("scatter plot")
# plt.show()


# BARPLOT
# categories=['A','B','C']
# values=[3,6,9]
# plt.bar(categories,values,color=['red','green','blue'])
# plt.title("bar plot")
# plt.show()


# HORIZONTAL BARPLOT
# categories=['A','B','C']
# values=[3,6,9]
# plt.barh(categories,values,color=['red','green','blue'])
# plt.title("horizontal bar plot")
# plt.show()

# HISTOGRAM
# data=np.random.randn(200000)
# plt.hist(data,bins=30,color='blue',edgecolor='black')
# plt.title("histogram")
# plt.show()


# PIECHART
# sizes=[20,30,25,25]
# labels=['A','B','C','D']
# plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
# plt.title("pie chart")
# plt.show()


# STACKED AREA PLOT
# days=[1,2,3,4,5]
# sleeping=[7,8,6,11,7]
# eating=[2,3,4,5,6]
# working=[7,8,9,6,4]
# playing=[11,10,3,2,8]
# plt.stackplot(days,sleeping,eating,working,playing,labels=['sleep','eat','work','play'])
# plt.legend(loc='upper left')
# plt.title("stacked area plot")
# plt.show()


# BOX PLOT
data=np.random.normal(100,20,200)
plt.boxplot(data)
plt.title("box plot")
plt.show()