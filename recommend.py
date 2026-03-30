import pandas as pd

def recommend_meals(tdee, user_goal):
    # Just printing some breadcrumbs to see where the code is
    print("--- Starting Meal Recommendation ---")
    
    try:
        # Load the csv from the data folder
        # Make sure the file path is correct!
        food_df = pd.read_csv("data/food.csv")
        print("Success: Loaded food.csv")
        # print(food_df.head()) # commented this out for now
    except Exception as err:
        print(f"Error: Could not find or read the CSV file. {err}")
        return None

    # Logic to filter based on the goal
    # A student might just use a fraction of the TDEE per meal
    target_per_meal = tdee / 3 
    print(f"Targeting about {int(target_per_meal)} calories per meal...")

    if user_goal == "lose":
        # Look for lighter options
        filtered_list = food_df[food_df["Calories"] < (target_per_meal - 100)]
    elif user_goal == "gain":
        # Look for high calorie options
        filtered_list = food_df[food_df["Calories"] > (target_per_meal + 100)]
    else:
        # Just stay around the target
        filtered_list = food_df[(food_df["Calories"] >= target_per_meal - 150) & 
                                (food_df["Calories"] <= target_per_meal + 150)]

    print(f"Found {len(filtered_list)} meals that match your goal.")

    # If the filter was too strict and we got nothing, just give back some random ones
    if len(filtered_list) == 0:
        print("Warning: No exact matches found. Just picking some random meals.")
        return food_df.sample(3)

    # Return 3 random meals from our filtered list
    # Use min() just in case the list is smaller than 3
    final_picks = filtered_list.sample(n=min(3, len(filtered_list)))
    
    return final_picks