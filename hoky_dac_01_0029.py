# -*- coding: utf-8 -*-
"""Hoky_DAC-01-0029

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ewDGlA1ZmyCS49FK3_dzuKomhfO9gpIP

# Library
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder

"""# Data Preprocessing"""

dataprediction=pd.read_csv('/content/Data_Prediction.csv', sep=';')
datatrain=pd.read_csv('/content/DataTrain_Preliminary.csv', sep=';')

dataprediction

datatrain

"""Information about the dataframe"""

datatrain.info()

dataprediction.info()

"""# Data Cleansing

Cleansing Data Prediction
"""

dataprediction.describe()

cat_cols = list(dataprediction.select_dtypes('object'))
cat_cols

"""There are 4 categorical data"""

num_cols = list(dataprediction.select_dtypes(exclude="object"))
num_cols

"""There are 35 numerical data"""

dataprediction_clean = dataprediction[(datatrain != '*').all(axis=1)]
print(dataprediction_clean)

"""We remove all of missing values."""

dataprediction_clean.info()

dataprediction_clean.head()

dataprediction_clean.isna().sum()

"""Cleansing Data Train"""

datatrain.describe()

cat_cols = list(datatrain.select_dtypes('object'))
cat_cols

"""There are 37 categorical data"""

num_cols = list(datatrain.select_dtypes(exclude="object"))
num_cols

"""there are 4 numerical data"""

unique_entries = datatrain.nunique()
print(unique_entries)

unique = datatrain['duration'].value_counts()
unique

"""There are 557 records that are * , we can consider them as missing values"""

datatrain_clean = datatrain[datatrain['duration'] != '*']
print(datatrain_clean)

"""We decided to deleted the missing values"""

datatrain_clean = datatrain[(datatrain != '*').all(axis=1)]
print(datatrain_clean)

"""We also removed all missing values "*" in all data."""

datatrain_clean.info()

datatrain_clean.isna().sum()

"""Re-check the missing value.

# Exploratory Data Analysis
"""

plt.figure(figsize=(15, 6))
sns.countplot(data=datatrain_clean, x="type_of_attack")
plt.title("Type of attack Distribution", fontsize=20)
plt.show()

datatrain_clean[num_cat_type_of_attack].info

num_cat_type_of_attack = ['dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_serror_rate','type_of_attack']
sns.pairplot(datatrain_clean[num_cat_type_of_attack], hue="type_of_attack")
plt.show()

"""More "normal" types of attacks than others"""

plt.figure(figsize=(10, 6))
sns.countplot(data=datatrain_clean, x='protocol_type', hue='type_of_attack')
plt.title("Type of attack distribution based on Protocol Type", fontsize=20)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=datatrain_clean, x='logged_in', hue='type_of_attack')
plt.title("Type of attack distribution based on Logged in", fontsize=20)
plt.show()

"""Details : (1 if yes, 0 if no).
Attack type based on number of logins. It was noted that the highest number of normal attacks were logged.
"""

plt.figure(figsize=(10, 6))
sns.countplot(data=datatrain_clean, x='wrong_fragment', hue='type_of_attack')
plt.title("Type of attack distribution based on wrong_fragment", fontsize=20)
plt.show()

"""The number of "wrong" fragments in a connection"""

fig = px.imshow(datatrain_clean.corr(),text_auto=True, title="The relation between numeric feature")
fig.show()

"""# Encoding
Encoding datatrain_clean
"""

datatrain_clean.head()

datatrain_clean.info()

label_encoders = {}

for kolom in datatrain_clean.columns:
   if kolom != 'type_of_attack' and datatrain_clean[kolom].dtype == 'object':  # Pastikan hanya kolom bertipe objek yang di-encode
        label_encoders[kolom] = LabelEncoder()
        datatrain_clean[kolom] = label_encoders[kolom].fit_transform(datatrain_clean[kolom])

"""Encoding is used to change the object data type to numeric."""

print(datatrain_clean)

datatrain_clean.info()

datatrain_clean.head()

"""Encoding dataprediction_clean"""

label_encoders2 = {}

for kolom in dataprediction_clean.columns:
 if dataprediction_clean[kolom].dtype == 'object':  # Pastikan hanya kolom bertipe objek yang di-encode
        label_encoders2[kolom] = LabelEncoder()
        dataprediction_clean[kolom] = label_encoders2[kolom].fit_transform(dataprediction_clean[kolom])

"""Encoding is used to change the object data type to numeric."""

dataprediction_clean.info()

"""Change the NaN data type in the numeric data type to mode"""

modus_value = datatrain_clean['dst_host_same_srv_rate'].mode().iloc[0]  # Mengambil modus pertama
datatrain_clean['dst_host_same_srv_rate'].fillna(modus_value, inplace=True)

modus_value = datatrain_clean['dst_host_diff_srv_rate'].mode().iloc[0]  # Mengambil modus pertama
datatrain_clean[ 'dst_host_diff_srv_rate'].fillna(modus_value, inplace=True)

modus_value = datatrain_clean['dst_host_same_src_port_rate'].mode().iloc[0]  # Mengambil modus pertama
datatrain_clean['dst_host_same_src_port_rate'].fillna(modus_value, inplace=True)

modus_value = datatrain_clean['dst_host_serror_rate'].mode().iloc[0]  # Mengambil modus pertama
datatrain_clean['dst_host_serror_rate'].fillna(modus_value, inplace=True)

datatrain_clean.head()

"""# SVM Model




"""

#Split data to x_train and y_train
x_train = datatrain_clean[['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
 'dst_host_srv_rerror_rate']]

y_train = datatrain_clean['type_of_attack']

x_prediction = dataprediction_clean[['duration', 'protocol_type', 'service' ,'flag' ,'src_bytes', 'dst_bytes',
 'land', 'wrong_fragment' ,'urgent' ,'hot' ,'num_failed_logins', 'logged_in',
 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
 'num_file_creations' ,'num_shells' ,'num_access_files', 'num_outbound_cmds',
 'is_host_login' ,'is_guest_login' ,'count' ,'srv_count' ,'serror_rate',
 'srv_serror_rate' ,'rerror_rate' ,'srv_rerror_rate', 'same_srv_rate',
 'diff_srv_rate', 'srv_diff_host_rate' ,'dst_host_count',
 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
 'dst_host_srv_rerror_rate']]

svm_model=SVC(kernel='linear',C=1.0)
svm_model.fit(x_train,y_train)

type_of_attack = svm_model.predict(x_prediction)

dataprediction_clean['type_of_attack'] = type_of_attack

print(type_of_attack)

num_predictions = len(type_of_attack)
print("The number of contents of the prediction:", num_predictions)

for prediction in type_of_attack:
    print(prediction)

unique_predictions = []
for prediction in type_of_attack:
    if prediction not in unique_predictions:
        unique_predictions.append(prediction)
print(unique_predictions)

unique = dataprediction_clean['type_of_attack'].value_counts()
unique

plt.figure(figsize=(15, 6))
sns.countplot(data=dataprediction_clean, x="type_of_attack")
plt.title("The Prediction of Type of Attack Distribution", fontsize=20)
plt.show()

# Simpan ke dalam file Excel (misalnya, 'data.xlsx')
dataprediction_clean.to_excel('ThePredictionResult.xlsx', index=False)  # index=False menghilangkan indeks dari DataFrame