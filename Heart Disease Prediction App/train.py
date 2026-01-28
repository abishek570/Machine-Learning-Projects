import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pathlib import Path
from joblib import dump

# Dataset with Feature variables (X) and Dependent variable(y)
data = pd.read_csv("heart.csv")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Spliting the data to Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Train the model with Logistic Regression
BASE_DIR = Path(__file__).parent
model_dir = Path(BASE_DIR / "model")
model_dir.mkdir(exist_ok=True)

regressor = LogisticRegression()
regressor.fit(X_train, y_train)

# Saving model in the model folder
dump(regressor, "model/Heart_disease_model.joblib")
print("Model training completed and saved to model/Heart_disease_model.joblib")
