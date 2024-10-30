# services.py
from sklearn.linear_model import LogisticRegression
import numpy as np

def stratify_risk(patient_data):
    model = LogisticRegression()
    X_train = np.array([[50], [60], [70], [80], [90]])
    y_train = np.array([0, 0, 1, 1, 1])
    model.fit(X_train, y_train)

    features = np.array([[patient_data['age']]])
    return model.predict_proba(features)[:, 1]
