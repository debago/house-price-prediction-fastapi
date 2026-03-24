import pandas
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
from mlflow.models import infer_signature


# set the tracking URL

mlflow.set_tracking_uri("http://localhost:5000")