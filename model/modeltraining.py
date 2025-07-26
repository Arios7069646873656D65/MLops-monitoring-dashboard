import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    with mlflow.start_run():
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        acc = accuracy_score(y_test, y_pred)

        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", acc)

        joblib.dump(clf, "model.pkl")
        mlflow.sklearn.log_model(clf, "random_forest_model")

        print(f"Model trained accuracy {acc:.2f}")

if __name__ == "__main__":
    main()