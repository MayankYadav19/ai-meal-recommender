# Ai-Meal-Recommender
“An AI-based system that calculates BMI and daily calorie needs and recommends personalized meal plans based on user goals such as weight loss, maintenance, or gain.”

# Overview
This project is a simple AI-based meal recommendation system that helps users understand their health and suggests meals based on their fitness goals.

The system calculates:
- BMI (Body Mass Index)
- BMR (Basal Metabolic Rate)
- TDEE (Total Daily Energy Expenditure)
- Machine Learning model (Decision Tree) for BMI classification
- Goal-based meal recommendation (lose/gain/maintain)
- Uses real dataset (food.csv)
- Command-line interface (CLI)

Based on these values, it recommends meals for:
- Weight Loss
- Weight Gain
- Maintenance
  
# Features
BMI calculation
Calorie Requirement (BMR & TDEE)
Meal Recommendation System
User Input Based System
# Technologies Used
Python
Pandas
Scikit-learn

# How It Works
User enters:
Weight
Height
Age
Gender
Activity level
System:
Calculates BMI
Uses ML model to predict category (underweight/normal/overweight/obese)
Decides goal automatically
Calculates calorie needs (TDEE)
Recommends meals based on goal

# Machine Learning
Model Used: Decision Tree Classifier
Input: BMI value
Output: Health category
Trained on sample labeled BMI dataset

This replaces traditional rule-based classification with a data-driven approach.

#  How to Run

# 1. Install dependencies
pip install pandas scikit-learn

# 2. Run the application
python app.py

# 3. Enter user details when prompted

Example:

Enter weight (kg): 60
Enter height (cm): 170
Enter age: 21
Enter gender (male/female): male
Activity level (low/moderate/high): moderate
# Example Output

BMI: 22.86
Category: Normal
Calories Needed: 2600 kcal

Recommended Meals:

Apple (80 kcal, Snack)
Rice (200 kcal, Lunch)
Eggs (155 kcal, Breakfast)

#  Dataset
The dataset is a CSV file containing food items with:
- Food name
- Calories
- Meal type

# Learnings
-Understanding of BMI, BMR, and TDEE calculations
-Basics of Machine Learning (Decision Tree)
-Data handling using Pandas
-Building a complete end-to-end project

# Future Improvements
-Add more food data
-Improve ML model with real dataset
-Add GUI (Streamlit / Web App)
-Personalized diet plans
