weight = float(input("Enter poatato weight in grams: "))
if weight <= 100:
    Grade = "Small"
elif weight > 100 and weight <= 200:
    Grade = "Medium"
else:
    Grade = "Large"
