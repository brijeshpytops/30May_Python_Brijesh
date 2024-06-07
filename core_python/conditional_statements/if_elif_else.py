score = float(input("Enter your score: "))

if score <= 100 and score >= 0:
    if score >= 80:
        print("FirstClass")
    elif score >= 60:
        print("SecondClass")
    elif score >= 40:
        print("ThirdClass")
    else:
        print("Sorry!, you are failed.")
else:
    print("Invalid score!, Please enter score between (0 to 100)")