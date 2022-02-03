
"""Health professionals who are helping a client achieve a healthy body weight,
sometimes use two computed measures named body mass index and basal metabolic rate.
From the U.S. Centers for Disease Control and Prevention we read,
 "Body mass index (BMI) is a person's weight in kilograms divided by the square of their height in meters. 
 BMI can be used to screen for weight categories such as underweight, normal, overweight, and obese that may lead to health problems.
  However, BMI is not diagnostic of the body fatness or health of an individual." The formula for computing BMI is
bmi = 10,000 weight / height2 """

from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    gender = input("Please enter your gender (M or F): ")
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in U.S. pounds: "))
    inches = float(input("Enter your height in U.S. inches: "))

    years = compute_age(birth_str)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi   = body_mass_index (kg, cm)
    bmr  = basal_metabolic_rate(gender, kg, cm, years)

    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg: .2f} ")
    print(f"Height (cm): {cm: .1f} ")
    print(f"Body mass index: {bmi: .1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr: .0f} ")


def compute_age(birth_str):
   
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kg = pounds * 0.45359237
    return kg


def cm_from_in(inches):
    cm= inches * 2.54 
    return cm


def body_mass_index(weight, height):
    #bmi = 10,000* weight /height**2
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    #(women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
    #(men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr

main()
