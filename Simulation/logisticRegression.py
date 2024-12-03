# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Example dataset: Hours Studied vs Passed Exam
# Hours studied (X) and target (y: 1=Pass, 0=Fail)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred_prob = model.predict_proba(X_test)[:, 1]  # Probability of class 1

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Visualize the sigmoid function
# Generate hours studied for prediction
X_vals = np.linspace(0, 7, 100).reshape(-1, 1)
y_probs = model.predict_proba(X_vals)[:, 1]

plt.figure(figsize=(8, 6))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X_vals, y_probs, color="red", label="Sigmoid Curve (Predicted Probability)")
plt.axhline(0.5, color="green", linestyle="--", label="Decision Boundary (0.5)")
plt.title("Logistic Regression: Hours Studied vs Passing Exam")
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()
