import pandas as pd
import numpy as np
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# ==========================
# LOAD DATA
# ==========================

df = pd.read_excel("../data/Overall Data.xlsx")

# ==========================
# CLEANING
# ==========================

df["Weight"] = pd.to_numeric(df["Weight"], errors="coerce")

df["Age (Month)"] = pd.to_numeric(
    df["Age (Month)"],
    errors="coerce"
)

df["Height"] = pd.to_numeric(
    df["Height"],
    errors="coerce"
)

df = df.dropna()

# ==========================
# FEATURE
# ==========================

X = df[
    [
        "Gender",
        "Age (Month)",
        "Weight",
        "Height"
    ]
]

y = df["Height for Age"]

# ==========================
# ENCODER
# ==========================

gender_encoder = LabelEncoder()
X["Gender"] = gender_encoder.fit_transform(X["Gender"])

target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# ==========================
# SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# MODEL
# ==========================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# EVALUASI
# ==========================

y_pred = model.predict(X_test)

metrics = {
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
    "f1": f1_score(y_test, y_pred),
    "cm": confusion_matrix(y_test, y_pred),
    "feature_importance": model.feature_importances_
}

# ==========================
# SAVE
# ==========================

joblib.dump(model, "model.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")
joblib.dump(gender_encoder, "gender_encoder.pkl")
joblib.dump(metrics, "metrics.pkl")

print("Model berhasil disimpan")