# Prompt the user to input their current age with the question: “How old are you? ”
your_age = int(input("How old are you? "))

Current_year = 2023  # You can also use datetime module to get the current year dynamically

age = (2050 - Current_year) + your_age

print(f"In 2050, you will be {age} years old.")

