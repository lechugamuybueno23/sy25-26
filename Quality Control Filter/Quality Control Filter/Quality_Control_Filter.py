all_potatoes = [0,2,5,1,0,8,3,0]
perfect_potatoes = []
for p in all_potatoes:
    if p == 0:
        perfect_potatoes.append(p)
num_total = len(all_potatoes)
num_perfect = len(perfect_potatoes)
percentage = (num_perfect / num_total) * 100
print(f"batch quality: {percentage}% perfect")
print(f"perfect potatoes found: {perfect_potatoes}")