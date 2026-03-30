# Function to find the BMI
def get_bmi(w, h):
    # change height from cm to meters
    meters = h / 100
    res = w / (meters * meters)
    return round(res, 2)

# Figure out the category based on the score
def check_category(bmi_score):
    if bmi_score < 18.5:
        return "underweight"
    if 18.5 <= bmi_score < 25:
        return "normal"
    if 25 <= bmi_score < 30:
        return "overweight"
    else:
        return "obese"

# BMR calculation using the Mifflin-St Jeor Equation
def find_bmr(weight, height, age, gender):
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        # formula for females is different
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

def get_tdee(bmr, activity_type):
    # multipliers for activity levels
    if activity_type == "low":
        return bmr * 1.2
    elif activity_type == "moderate":
        return bmr * 1.55
    elif activity_type == "high":
        return bmr * 1.9
    else:
        return bmr # default case if input is weird