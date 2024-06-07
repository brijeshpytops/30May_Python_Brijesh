from datetime import datetime

day = datetime.now().weekday()

# import datetime
# print(datetime.datetime.now())
# day = 12
match day:
    case 0:
        print("Today is Mon")
    case 1:
        print("Today is Tue")
    case 2:
        print("Today is Wed")
    case 3:
        print("Today is Thu")
    case 4:
        print("Today is Fri")
    case 5:
        print("Today is Sat")
    case 6:
        print("Today is Sun")
    case _:
        print("Invalid day")