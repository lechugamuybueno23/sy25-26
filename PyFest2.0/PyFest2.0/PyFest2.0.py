lineup = []

while True:
    print("--- Py-fest 2026 Stage Manager ---")
    print("1. View lineup & total time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove a Band by Name")
    print("5. Move Band to Specific Position")
    print("6. Exit")
    choice = input("Select an option (1-6): ")

  


    #Parts
    if choice == "1":
        print("\n--- Current Lineup ---")
        for i, band in enumerate(lineup, 1):
            print(f"{i}. {band}")
        print(f"Total bands: {len(lineup)}")
    elif choice == "2":
        name = input("Enter band name: ")
        lineup.append(name)
        print(f"{name} added to the lineup.")
    elif choice == "3":
         if lineup:
            band = lineup.pop(0)
            lineup.append(band)
            print(f"{band} moved to the end of the lineup.")
         else:
            print("Lineup is empty.")
    elif choice == "4":
         name = input("Enter the name of the band to remove: ")
         if name in lineup:
            lineup.remove(name)
            print(f"{name} removed from the lineup.")
         else:
            print(f"{name} not found in the lineup.")
    elif choice == "5":
        name_to_move = input("Enter the name of the band to move: ")
        if name_to_move in lineup:
            new_pos = int(input("Enter the new position (1-based): ")) - 1
            lineup.remove(name_to_move)
            lineup.insert(new_pos, name_to_move)
            print(f"{name_to_move} moved to position {new_pos + 1}.")
        else:
            print(f"{name_to_move} not found in the lineup.")
    elif choice == "6":
        print("Exiting Stage Manager.")
        break
    else:
        print("Invalid option. Please select 1-6.")