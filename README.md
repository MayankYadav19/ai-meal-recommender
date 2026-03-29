# AI Meal Recommender

## Overview

This project is a simple meal recommendation system built using basic AI and ML concepts. The idea came from a common problem — people often don’t know what to eat based on their health goals.

In this project, I calculate BMI, predict the health category using a machine learning model, and then suggest meals based on calorie needs.

While working on this project, I also got a better understanding of how health calculations and ML can be combined in a real-world example.

---

## Features

* Calculates BMI
* Calculates BMR and TDEE (daily calories needed)
* Uses a simple ML model (Decision Tree)
* Automatically decides goal (lose/gain/maintain)
* Suggests meals from a dataset
* Runs in command line

---

## How it works

First, the user enters:

* weight
* height
* age
* gender
* activity level

Then the system:

* calculates BMI
* predicts category using ML
* decides the goal automatically
* calculates daily calories
* recommends meals

---

## Machine Learning part

For the ML part, I used a Decision Tree model.

* Input: BMI value
* Output: category (underweight, normal, overweight, obese)

At first, I was a bit confused about how to actually use ML in this project, but after trying it practically, I understood that instead of writing many if-else conditions, the model can learn from data.

---

## Project Structure

ai-meal-recommender/

app.py → main file

src/

* health.py → BMI, BMR, TDEE calculations
* recommend.py → meal recommendation logic
* model.py → ML model

data/

* food.csv → dataset

---

## How to run

1. Install required libraries
   pip install pandas scikit-learn

2. Run the program
   python app.py

3. Enter details when asked

---

## Example output

BMI: 22.8
Category: normal
Goal: maintain
Calories: 2600

Meals:

* Apple
* Rice
* Eggs

---

## Dataset

The dataset is a simple CSV file which contains:

* food name
* calories
* meal type

---

## Challenges faced

While building this project, I faced some issues like:

* pandas not working at first
* CSV file errors
* confusion while connecting ML with the main code

I solved these by debugging step by step and checking errors carefully.

---

## What I learned

* Basics of BMI, BMR, and calorie calculations
* How a simple ML model works
* Using pandas for data handling
* Debugging and connecting different parts of a project

---

## Future improvements

* Add more food items
* Improve ML model with better dataset
* Add a simple UI (Streamlit or web app)

---

## Author

Mayank Yadav
