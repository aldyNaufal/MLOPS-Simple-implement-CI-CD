import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from joblib import dump
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data-path", type=str, required=True, help="Path to the training data CSV")
args = parser.parse_args()

print("Loading data...")
df = pd.read_csv(args.data_path, header=0)

X = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Evaluating model...")
predictions = model.predict(X_test)
report = classification_report(y_test, predictions)

print("Evaluation Report:")
print(report)

print("Saving artifacts...")
dump(model, 'model.joblib')

# Simpan laporan evaluasi
with open('evaluation.txt', 'w') as f:
    f.write(report)

print("Workflow completed successfully.")