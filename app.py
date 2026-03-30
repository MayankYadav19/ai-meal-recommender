import src.health as health
import src.recommend as rec
import src.model as model

print("--- HEALTH APP STARTING ---")

# Getting user data from the console
try:
    # Adding .strip() helps if the user accidentally hits space
    w_input = input("Enter weight in kg: ")
    weight = float(w_input)
    
    h_input = input("Enter height in cm: ")
    height = float(h_input)
    
    a_input = input("Enter your age: ")
    age = int(a_input)
    
    gender = input("Gender (male/female): ").lower().strip()
    activity = input("Activity level (low/moderate/high): ").lower().strip()

    # 1. Calculating the BMI first
    bmi_val = health.get_bmi(weight, height)
    print(f"\n> Your calculated BMI is: {bmi_val}")

    # 2. Use the ML model to predict the category
    # (Hope the model is trained well!)
    pred_cat = model.predict_bmi_category(bmi_val)
    print(f"> ML Prediction says you are: {pred_cat}")

    # 3. Figure out if we need to lose, gain or stay the same
    if pred_cat == "underweight":
        user_goal = "gain"
    elif pred_cat == "overweight" or pred_cat == "obese":
        user_goal = "lose"
    else:
        user_goal = "maintain"

    print(f"> Target Goal: {user_goal}")

    # 4. Calorie math
    user_bmr = health.find_bmr(weight, height, age, gender)
    user_tdee = health.get_tdee(user_bmr, activity)
    print(f"> Daily calories needed: {int(user_tdee)} kcal")

    # 5. Get the meal list
    print("\n--- Finding the best meals for you ---")
    suggested_meals = rec.recommend_meals(user_tdee, user_goal)

    if suggested_meals is not None and not suggested_meals.empty:
        # Loop through the rows to show the food items
        for index, row in suggested_meals.iterrows():
            food_name = row['Food']
            calories = row['Calories']
            m_type = row['MealType']
            print(f"* {m_type}: {food_name} ({calories} kcal)")
    else:
        print("Sorry, couldn't find any meal data in the CSV/database.")

except ValueError:
    print("Error: Please make sure you enter numbers for weight, height, and age!")
except Exception as e:
    print(f"Something went wrong: {e}")