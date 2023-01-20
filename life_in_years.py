age = input("What is your current age?")

muerte = int(input("Until what age you plan to live?"))

age_float = int(age)
age_muerte = muerte - age_float

days = (365 * age_muerte)
weeks = (52 * age_muerte)
months = (12 * age_muerte)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")