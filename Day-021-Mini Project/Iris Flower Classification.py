# Iris Flower Classification using Decision Tree

# Import the Iris dataset
from sklearn.datasets import load_iris

# Import function to split data into training and testing sets
from sklearn.model_selection import train_test_split

# Import Decision Tree classification algorithm
from sklearn.tree import DecisionTreeClassifier

# Import evaluation metrics
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Load the Iris dataset
iris = load_iris()

# Store the input features
X = iris.data

# Store the target labels
y = iris.target

# Display the shape of features and target
print(X.shape)
print(y.shape)


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)


# Create the Decision Tree classification model
model = DecisionTreeClassifier(random_state=42)

# Train the model using the training data
model.fit(X_train, y_train)

# Predict the classes for the test data
y_pred = model.predict(X_test)


# Calculate the model accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display the accuracy
print("Accuracy:", accuracy)


# Generate and display the classification report
print("Classification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))


# Generate and display the confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Create a new flower with sepal and petal measurements
new_flower = [[5.1, 3.5, 1.4, 0.2]]

# Predict the species of the new flower
prediction = model.predict(new_flower)

# Display the predicted flower species
print("\nNew Flower Prediction:")
print(iris.target_names[prediction[0]])