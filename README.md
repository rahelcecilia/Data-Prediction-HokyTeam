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
### Data Preprocessing
```
dataprediction=pd.read_csv('/content/Data_Prediction.csv', sep=';')
datatrain=pd.read_csv('/content/DataTrain_Preliminary.csv', sep=';')
```
