import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from joblib import load

# Dataset with Feature variables (X) and Dependent variable(y)
data = pd.read_csv("heart.csv")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Spliting the data to Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Load the trained model
model = load("model/Heart_disease_model.joblib")

# Get predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Evaluating the model
print("=" * 50)
print("MODEL EVALUATION METRICS")
print("=" * 50)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {acc:.4f}")

# Precision
precision = precision_score(y_test, y_pred)
print(f"Precision Score: {precision:.4f}")

# Recall
recall = recall_score(y_test, y_pred)
print(f"Recall Score: {recall:.4f}")

# F1-Score
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1:.4f}")

# ROC-AUC Score
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"ROC-AUC Score: {roc_auc:.4f}")

print("=" * 50)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Create the display object
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])

# Plot the matrix
disp.plot(cmap=plt.cm.Blues)  # Use a colormap for better visualization
plt.title("Confusion Matrix")
# plt.savefig("plot.png")
plt.show()

