def farm():
    while True:
        name = input("Enter your name: ").capitalize()
        if name == "":
            print("Nume must not be empty")
            continue 
        elif name.isalpha():
            break 
        else:
            print("Enter a valid name ")


    #batch code validation must start with "GR" and end with three numbers e.g GR-OO1
    while True:
        Batch_ID = input("Enter Your famer Unique ID: ").upper().strip()
        if (not Batch_ID.startswith("GR-") or len(Batch_ID) != 6 or not Batch_ID[3:].isdigit()):
            print("Invalid Famers batch id")
            continue 
        else:
            print(f"Welcome {name}")
            break 

    crate_weight = []
    for i in range(4):
        while True:
            try:
                weight = float(input(F"{i+1} Enter the weight of crate: "))
                
                if 5 <= weight <= 50:
                    crate_weight.append(weight)
                    break
                else:
                    print("Weight must be between 5 to 50kg")

                
            except ValueError:
                print("Enter a valid nmber")  
    #selection logic 
    totat_weight = sum(crate_weight)
    average = totat_weight / 4 
    export_status = "Export Grade" if average > 30 else "Standard Grade"

    crate_lines = ""
    for i, weight in enumerate(crate_weight, start= 1):
        load_label = "Heavy Load " if weight > 40 else ""
        crate_lines += f"crate {i}: {weight:.2f}kg {load_label}"


    print()
    print("-" * 8 + "Output Summary" + "-" * 8 )
    print(f"\n Harvest Report \n"
            f"Famers name: {name}\n"
            f"Batch ID: {Batch_ID}\n"
            f"{'-' * 10 }\n"
            f"{crate_lines}\n"
            f"Total: {totat_weight}\n"
            f"Average Weight: {average}\n"
            f"Export status: {export_status}\n"
            f"{'-' * 40}")       
    
farm()