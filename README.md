# Data-Prediction-HokyTeam
Participating in DAC 2023 by HIMASTA-ITS at Statistic Fair 2023. Undergrads from Southeast Asia analyze real data, sharpen critical thinking for practical applications. Empowering future statisticians. 

## Library
```
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
```
## Data Information Gathering
This involves searching for available information from the existing
datasets. In this case, we have two datasets, namely the <strong>Training Data </strong> and
 <strong>Prediction Data </strong>. The data information gathering is useful to determine the data
types and the quantity of data available.

## Data Preprocessing
Within this stage, there are several steps, including:
<br>
### 1. Data Cleansing
Data cleansing aims to check the training and prediction data for
identifying and addressing issues such as missing data, duplicates, or
anomalies.
<br>
```
dataprediction=pd.read_csv('/content/Data_Prediction.csv', sep=';') 
datatrain=pd.read_csv('/content/DataTrain_Preliminary.csv', sep=';')
```
Use these codes to show the short review from the all data. <br>
```dataprediction``` ```datatrain```

Information about the dataframe <br>
```datatrain.info()``` ```dataprediction.info()```


#### Cleansing data prediction
Identify data type
```
#Categorical Data
cat_cols = list(dataprediction.select_dtypes('object'))
cat_cols
```
```
#Numerical Data
num_cols = list(dataprediction.select_dtypes(exclude="object"))
num_cols
```
Searching for data with a value * , and remove all.
```
dataprediction_clean = dataprediction[(dataprediction != '*').all(axis=1)]
print(dataprediction_clean)
```
Information about data after removing the missing values.
```
dataprediction_clean.info()
```
To check the number of empty data again.
```
dataprediction_clean.isna().sum()
```

#### Cleansing data train
Identify data type
```
#Categorical Data
cat_cols = list(datatrain.select_dtypes('object'))
cat_cols
```
```
#Numerical Data
num_cols = list(datatrain.select_dtypes(exclude="object"))
num_cols
```
To find unique values from the data
```
unique_entries = datatrain.nunique()
print(unique_entries)
```
To find unique values from the "duration" column. We can see in the duration column, there are 557 records that are (*) , we can consider them as missing values.
```
unique = datatrain['duration'].value_counts()
unique
```
We deleted the missing values from duration column
```
datatrain_clean = datatrain[datatrain['duration'] != '*']
print(datatrain_clean)
```
Searching for data with a value * , and remove all.
```
datatrain_clean = datatrain[(datatrain != '*').all(axis=1)]
print(datatrain_clean))
```
Information about data after removing the missing values.
```
datatrain_clean.info()
```
To check the number of empty data again.
```
datatrain_clean.isna().sum()
```




