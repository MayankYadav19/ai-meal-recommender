
#  AI Meal Recommender with Machine Learning

##  Overview

This project is an AI-based meal recommendation system that helps users understand their health status and suggests suitable meals based on their goals.

It calculates BMI, predicts health category using Machine Learning, estimates daily calorie needs, and recommends meals accordingly.

---

##  Features

* BMI Calculation
* BMR & TDEE (daily calorie needs) calculation
* Machine Learning model (Decision Tree)
* Automatic goal detection (lose/gain/maintain)
* Goal-based meal recommendation
* Uses dataset (`food.csv`)
* Command-line interface (CLI)

---

##  How It Works

1. User enters:

   * Weight
   * Height
   * Age
   * Gender
   * Activity level

2. System:

   * Calculates BMI
   * Uses ML model to predict category (underweight/normal/overweight/obese)
   * Automatically decides goal
   * Calculates calorie needs (TDEE)
   * Recommends meals based on goal

---

##  Machine Learning

* Model Used: **Decision Tree Classifier**
* Input: BMI value
* Output: Health category
* Trained on sample labeled BMI dataset

This replaces traditional rule-based classification with a simple data-driven approach.

---

##  Project Structure

```plaintext
ai-meal-recommender/
│
├── app.py                # Main application
│
├── src/
│   ├── health.py         # BMI, BMR, TDEE calculations
│   ├── recommend.py      # Meal recommendation logic
│   └── model.py          # ML model for BMI prediction
│
└── data/
    └── food.csv          # Food dataset
```

---

##  How to Run

### 1. Install dependencies

```bash
pip install pandas scikit-learn
```

---

### 2. Run the application

```bash
python app.py
```

---

### 3. Enter user details

Example:

```plaintext
Enter weight (kg): 60  
Enter height (cm): 170  
Enter age: 21  
Enter gender (male/female): male  
Activity level (low/moderate/high): moderate  
```

---

##  Example Output

```plaintext
BMI: 22.86  
Category (ML): normal  
Goal: maintain  
Calories needed: 2600  

Recommended Meals:

- Apple (80 kcal, Snack)  
- Rice (200 kcal, Lunch)  
- Eggs (155 kcal, Breakfast)  
```

---

##  Dataset

The dataset is a CSV file containing:

* Food name
* Calories
* Meal type

---

##  Learnings

* Understanding of BMI, BMR, and TDEE calculations
* Basics of Machine Learning (Decision Tree)
* Data handling using Pandas
* Building a complete end-to-end project

---

##  Future Improvements

* Add more food data
* Improve ML model with real dataset
* Add GUI (Streamlit / Web App)
* Personalized diet plans

---

##  Author

* Mayank Yadav

---

##  Note

This project was built as part of an **AI/ML learning project** and demonstrates how basic machine learning can be integrated into a real-world application.

---

