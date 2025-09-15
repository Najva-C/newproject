import pandas as pd
import numpy ad np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinesrRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


columns = ['buying','maint','doors','persons','lug_boot','safety','class']
df = pd.read_csv("car.data",names = columns)
print("null value under each column")
print(df.isnull().null())
x = df.drop(column=["class"])
y = df["class"]
label_encoder ={}
for column in  df.columns:
    le = {}
    df[column] = le.fit_transform(df{column})
    label_encoder[column] = le
