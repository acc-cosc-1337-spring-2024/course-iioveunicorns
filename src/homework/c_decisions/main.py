#

from decisions import get_options_ratio, get_faculty_rating

options = float(input("Enter the number of options: "))
total = float(input("Enter the total number: "))

ratio = get_options_ratio(options, total)

faculty_rating = get_faculty_rating(ratio)

print("Faculty Rating:", faculty_rating)
