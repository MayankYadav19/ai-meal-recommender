# Ai-Meal-Recommender
“An AI-based system that calculates BMI and daily calorie needs and recommends personalized meal plans based on user goals such as weight loss, maintenance, or gain.”

# Overview
This project is a simple AI-based meal recommendation system that helps users understand their health and suggests meals based on their fitness goals.

The system calculates:
- BMI (Body Mass Index)
- BMR (Basal Metabolic Rate)
- TDEE (Total Daily Energy Expenditure)

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

# Project Structure

ai-meal-recommender/
│
├── app.py
├── README.md
├── data/
│ └── food.csv
├── src/
│ ├── init.py
│ ├── health.py
│ └── recommend.py

#  How to Run

1. Install dependencies:

pip install pandas


2. Run the application:

python app.py


3. Enter your details:
- Weight
- Height
- Age
- Gender
- Activity Level
- Goal

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

# Future Improvements
- Expand food dataset
- Build a web interface (using Flask/Streamlit)
- Add user history tracking

# Learnings
- Understanding of BMI, BMR, and TDEE
- Working with real-world datasets
- Python modular coding (multiple files)
- Debugging and project structuring
