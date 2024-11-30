import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

column_names = [
    "erythema", "scaling", "definite_borders", "itching", "koebner_phenomenon",
    "polygonal_papules", "follicular_papules", "oral_mucosal_involvement",
    "knee_elbow_involvement", "scalp_involvement", "family_history", "age", "class"
]
data = pd.read_csv("dermatology.data", header=None, names=column_names, na_values=["?"])

imputer = SimpleImputer(strategy="most_frequent")
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

X = data_imputed.drop(columns=['class'])
y = data_imputed['class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def perform_cross_validation(X, y, model, n_splits=10):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
    cv_scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
    print(f"Cross-validation accuracy scores: {cv_scores}")
    print(f"Mean accuracy: {np.mean(cv_scores)}")

def train_and_evaluate(X_train, X_test, y_train, y_test, model):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()
    
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=5)
perform_cross_validation(X_scaled, y, knn)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

train_and_evaluate(X_train, X_test, y_train, y_test, knn)

param_grid = {'n_neighbors': np.arange(1, 21)}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print("Best K for KNN: ", grid_search.best_params_)
print("Best accuracy score: ", grid_search.best_score_)
