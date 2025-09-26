import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.compose import ColumnTransformer


# LOAD DATA
data = pd.read_csv("NUMPY/student_performance_dataset.csv")
print(data.head())

# CHECK FOR NULL VALUES
print(data.isnull().sum())

# ENCODING
# preprocessor = ColumnTransformer(transformers=[("enc",OneHotEncoder(),['Gender'])])
# transformed_data = preprocessor.fit_transform(preprocessor)
# print(data.head())

data['Gender'] = data['Gender'].map({'Male':0,'Female':1})
data['Internet_Access_at_Home'] = data['Internet_Access_at_Home'].map({'No':0,'Yes':1})
data['Extracurricular_Activities'] = data['Extracurricular_Activities'].map({'No':0,'Yes':1})
data['Pass_Fail'] = data['Pass_Fail'].map({'Pass':1,'Fail':0})
print(data.head())
print(data.isnull().sum())

data = data.drop('Student_ID',axis=1)

x = data[['Gender','Study_Hours_per_Week','Attendance_Rate','Internet_Access_at_Home','Extracurricular_Activities','Final_Exam_Score']]
y = data['Pass_Fail']


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(f"Accuracy: ",accuracy_score(y_pred,y_test))
print(f"Classification Report: ",classification_report(y_pred,y_test))
print(f"Confusiion Matrix: ",confusion_matrix(y_pred,y_test))








