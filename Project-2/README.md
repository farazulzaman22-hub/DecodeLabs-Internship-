# 🌸 Iris Flower Classification Using AI

**Project 2 | DecodeLabs AI Internship – Batch 2026**

## 📌 Overview

This project is the predictive phase of the DecodeLabs AI Internship — moving beyond rule-based logic (Project 1) into **Supervised Learning**. It builds a classification model that learns to recognize patterns in flower measurement data and predicts the species of new, unseen flowers.

The model is trained on the classic **Iris dataset**, a well-known benchmark in machine learning, and uses the **K-Nearest Neighbors (KNN)** algorithm to classify flowers into one of three species based on their physical measurements.

## ✨ Features

- **Dataset Loading & Exploration** – Loads the built-in Iris dataset (150 samples, 4 features, 3 classes) and displays its structure.
- **Feature Scaling** – Uses `StandardScaler` to normalize all features to the same range (mean = 0, variance = 1), preventing any single feature from dominating the model.
- **Train-Test Split** – Splits the data into 80% training and 20% testing sets with a fixed random seed for reproducibility.
- **KNN Classification Model** – Trains a K-Nearest Neighbors classifier (K=5) that predicts a flower's species based on the 5 most similar flowers in the training data.
- **Model Evaluation** – Reports accuracy, a confusion matrix, and a full classification report (precision, recall, F1-score) for each species.
- **Interactive Prediction Tool** – Lets the user input their own flower measurements and get a real-time species prediction, with input validation and a continuous loop to test multiple flowers.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries Used:** `scikit-learn`, `pandas` (environment), `numpy` (via scikit-learn)
- **Algorithm:** K-Nearest Neighbors (KNN)
- **Core Concepts:** Supervised learning, feature scaling, train-test split, model evaluation metrics

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Install the required library:

   ```bash
   pip install scikit-learn
   ```

3. Open a terminal in the project directory.
4. Run the following command:

   ```bash
   python iris_classification.py
   ```

5. The script will train the model and print evaluation results automatically.
6. You'll then be prompted to test your own flower measurements — type `yes` to enter sepal/petal length and width, or `no` to exit.

## 💬 Example Output

```
Dataset Shape: (150, 4)
Feature Names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Target Classes: ['setosa' 'versicolor' 'virginica']

Training set size: (120, 4)
Testing set size: (30, 4)

Model Accuracy: 1.0

Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

Classification Report:
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00         9
   virginica       1.00      1.00      1.00        11

Do you want to predict a new flower? (yes/no): yes
Enter Sepal Length (cm): 5.1
Enter Sepal Width (cm): 3.5
Enter Petal Length (cm): 1.4
Enter Petal Width (cm): 0.2

🌸 Predicted Species: SETOSA
```

## 📂 Project Structure

```
Project-2/
│
├── iris_classification.py   # Main classification script
└── README.md                 # Project documentation
```

## 🧠 Key Learnings

This project reinforced the importance of:

- **The Input → Process → Output (IPO) pipeline** as the foundational blueprint for any machine learning system.
- **Feature scaling** as a critical preprocessing step — without it, models can be biased toward features with larger numeric ranges.
- **Why accuracy alone isn't enough** — the "Accuracy Mirage" on imbalanced datasets means metrics like precision, recall, and the confusion matrix are essential for a true picture of model performance.
- **The train-test split** as the mechanism that proves a model can generalize to new data, not just memorize what it has already seen.
- **Applying the same transformation** (scaler) consistently to both training and new/unseen data to ensure valid predictions.

## 🔮 Future Improvements

- Experiment with different values of K to find the optimal number of neighbors (the "elbow point").
- Compare KNN against other classification algorithms (Decision Trees, Logistic Regression, SVM).
- Test the model on a different, more complex dataset with imbalanced classes.
- Visualize the decision boundaries and data distribution using matplotlib.

---

**Author:** Faraz
**Internship:** DecodeLabs AI Internship – Batch 2026
**Project:** 2 of N – Data Classification Using AI
