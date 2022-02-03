import math 
from datetime import datetime

width = int(input("Enter the width of the tire in mm (ex 205): "))

ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume_liters = ((math.pi * width ** 2) * (ratio * (width * ratio + 2540 * diameter)))/10000000000

print(f"The aproximate volume is {volume_liters:.2f} liters")
print()
# opening a file and appending to the end of a text file.

current_date_and_time = datetime.now()


# core requierements, commenting line 20 to proceed with core requierements
# with open("volumes.txt", mode="at") as tire_volumes:

    # core requierements to append inf to file name volumes.txt commenting line 21 to proceed with exceeding requierements.
    # print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume_liters:.2f}", file=tire_volumes)
    
buy = input("Do you want to buy the tire with the dimensions entered? ").lower()

if buy == "yes":
    phone_number = input("Please enter phone number: ")
    with open("volumes.txt", mode="at") as tire_volumes:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume_liters:.2f}, {phone_number}", file=tire_volumes)
else:
    with open("volumes.txt", mode="at") as tire_volumes:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume_liters:.2f}", file=tire_volumes)

