from datetime import date  
today = date.today()  
date_str = str(today)
def get():
    nme = input("whats the name of an item? ")
    amt = float(input("whats the amount? "))
    file.write(f"{nme},{amt},{date_str}\n")
    print("saved to file")
while True: 
    with open("expenses.csv", "a") as file:  
        print("Hi, bank thingy")
        ques = input("1. add to list 2. look at all expenses 3. end 4. delete: ")
        if ques == "1":
            get()
        if ques == "2":
            with open("expenses.csv", "r") as file:  
                lines = file.readlines()  
                for line in lines:  
                    print(line.strip())  

        if ques == "3":
            break
                        
        if ques == "4":
            check = input("are you sure you want to clear everything? type: Yesmedelete: ")
            if check == "Yesmedelete":
                with open("expenses.csv", "w") as file:  
                 pass 
            else:
                print("ok")

