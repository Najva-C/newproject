import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

data = pd.read_csv("NUMPY/Adult Data.csv")
print(data.head())
print(data.isnull().sum())



x =data[[]]
y =data[]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(f"Accuracy: ",accuracy_score(y_pred,y_test))
print(f"Classification Report: ",classification_report(y_pred,y_test))
print(f"Confusiion Matrix: ",confusion_matrix(y_pred,y_test))