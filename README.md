# Data-Prediction-HokyTeam
Participating in DAC 2023 by HIMASTA-ITS at Statistic Fair 2023. Undergrads from Southeast Asia analyze real data, sharpen critical thinking for practical applications. Empowering future statisticians. 

### Library
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
### Data Information Gathering
This involves searching for available information from the existing
datasets. In this case, we have two datasets, namely the <strong>Training Data </strong> and
 <strong>Prediction Data </strong>. The data information gathering is useful to determine the data
types and the quantity of data available.

### Data Preprocessing
Within this stage, there are several steps, including:
<li><strong>Data Cleansing</strong></li>
<br>
Data cleansing aims to check the training and prediction data for
identifying and addressing issues such as missing data, duplicates, or
anomalies.
<br>

dataprediction=pd.read_csv('/content/Data_Prediction.csv', sep=';') <br>
datatrain=pd.read_csv('/content/DataTrain_Preliminary.csv', sep=';')


<br>
Use this code to show the short review from the all data. <br>
```dataprediction``` ```datatrain```

