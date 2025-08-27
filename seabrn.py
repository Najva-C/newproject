import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# # HISTOGRAM + KDE
# df = sns.load_dataset("tips")
# sns.histplot(df["total_bill"],bins=20,kde=True,color="skyblue")
# plt.title("histogram + KDE")
# plt.show()


# # BAR PLOT(WITH ERROR BARS)
# data = pd.DataFrame({
#     "category":['A','B',"C",'D'],
#     "value":[4,7,2,9]
# })
# sns.barplot(x="category",y="value",data=data)
# plt.title("normal bar chart (seaborn)")
# plt.show()


# # COUNT OF CATEGORIES PLOT
# df = sns.load_dataset("tips")
# sns.countplot(x="day",data=df,palette="Set2")
# plt.title("count plot")
# plt.show()



# BOX PLOT
# df = sns.load_dataset("tips")
# sns.boxplot(x="day",y="total_bill",data=df,palette="pastel")
# plt.title("box plot")
# plt.show()


# SCATTER PLOT
df = sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=df,hue="sex",style="time")
plt.title("scatter plot")
plt.show()
