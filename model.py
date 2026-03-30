import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Making a simple dataset for the model to learn from
# (Added a few more points so the tree isn't too small)
data_dict = {
    "bmi": [15.5, 17, 18.2, 20.5, 22.1, 24.8, 25.5, 27.2, 29.5, 32.0, 35.5, 38.0],
    "label": [
        "underweight", "underweight", "underweight", 
        "normal", "normal", "normal", 
        "overweight", "overweight", "overweight",
        "obese", "obese", "obese"
    ]
}

# Load it into a dataframe
my_df = pd.DataFrame(data_dict)

# Features and Target
X_train = my_df[["bmi"]]
y_train = my_df["label"]

# Initialize the classifier - simple Decision Tree
# A student might leave the default settings
clf = DecisionTreeClassifier()

print("Training the BMI classification model...")
clf.fit(X_train, y_train)
print("Model trained successfully!")

def predict_bmi_category(user_bmi):
    # The model expects a DataFrame, so we wrap the single value
    # Using the same column name as before
    test_data = pd.DataFrame([[user_bmi]], columns=["bmi"])
    
    prediction = clf.predict(test_data)
    
    # Return the first item in the array (the string)
    return prediction

# Small test just to make sure it works before importing it elsewhere
# print(predict_bmi_category(22.5))