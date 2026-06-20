# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load the Iris dataset
iris = load_iris()

# Features (the measurements) and target (the species labels)
X = iris.data
y = iris.target

# Print basic info to understand the dataset
print("Dataset Shape:", X.shape)
print("Feature Names:", iris.feature_names)
print("Target Classes:", iris.target_names)
print("First 5 rows of data:\n", X[:5])
print("First 5 labels:", y[:5])

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nBefore Scaling (first row):", X[0])
print("After Scaling (first row):", X_scaled[0])

# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# Create KNN model with K=5
model = KNeighborsClassifier(n_neighbors=5)

# Train model using the training data
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# Make predictions on the test set
y_pred = model.predict(X_test)

print("\nPredicted labels:", y_pred)
print("Actual labels:   ", y_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ============================================
# Interactive Prediction: Try your own flower!
# ============================================

print("\n" + "=" * 50)
print("Try predicting a new flower's species!")
print("=" * 50)

while True:
    user_choice = input("\nDo you want to predict a new flower? (yes/no): ").lower().strip()

    if user_choice in ["no", "n", "exit"]:
        print("Thanks for using the Iris Classifier. Goodbye!")
        break

    elif user_choice in ["yes", "y"]:
        try:
            sepal_length = float(input("Enter Sepal Length (cm): "))
            sepal_width = float(input("Enter Sepal Width (cm): "))
            petal_length = float(input("Enter Petal Length (cm): "))
            petal_width = float(input("Enter Petal Width (cm): "))

            # Combine inputs into the same format as training data
            new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

            # Scale the new input using the SAME scaler used for training
            new_flower_scaled = scaler.transform(new_flower)

            # Predict the species
            prediction = model.predict(new_flower_scaled)
            predicted_species = iris.target_names[prediction[0]]

            print(f"\n🌸 Predicted Species: {predicted_species.upper()}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

    else:
        print("Please type 'yes' or 'no'.")