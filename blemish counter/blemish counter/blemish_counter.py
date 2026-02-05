blemish_counts= []
for i in range(5):
    count = int(input(f"enter blemishes for potato {i+1}: "))
    blemish_counts.append(count)
total = sum(blemish_counts)
average = total / len(blemish_counts)
print(f"Total blemishes: {total}")
print(f"Average blemish per potato: {average}")
