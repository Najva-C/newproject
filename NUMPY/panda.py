import pandas as pd 

# SERIES
# s = pd.Series([10,20,30,40,50])
# print(s)

# DATAFRAME
data = {'name':['alice','bob','arya','abhi','krish','anu','sree'],'age':[25,30,44,33,77,55,None]}
# df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.head(4))


# print(df.tail())
# print(df.tail(2))

# df.info()

# print(df.describe())

# print(df.columns)

# print(df.shape)

df = pd.DataFrame(data,index=['a','b','c','d','e','f','g'])
print(df.loc['c'])
print(df.loc['d','name'])
print(df.loc[:,['name','age']])

print(df.iloc[1])
print(df.iloc[1,0])
print(df.iloc[:,0:2])

print(df.isnull())

print(df.dropna())

print(df.fillna(33))

# df['Age'].fillna(df['Age'].mean(),inplace=True)
# print(df)

