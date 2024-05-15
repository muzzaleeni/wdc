
#importing all the neccessary dependencies and libraries
from .queries import *

def select_query():
    print("Select a query option:")
    print("1. AvgLandTemp")
    print("2. AvgTemperatureColor")
    print("3. C3S_satellite_soil_moisture_active_daily_sensor")
    print("4. RadianceColorScaled")

    option = input("Enter your choice: ")

    if option == "1":
        run_query(query1)
        run_query(query2)
        run_query(query4)
        run_query(query5)
        run_query(query6)
        run_query(query7)
    elif option == "2":
        run_query(query8)
        run_query(query9)
        run_query(query10)
        run_query(query11)
        run_query(query12)
    elif option == "3":
        run_query(query13)
        run_query(query14)
        run_query(query15)
        run_query(query16)
        run_query(query17)
    elif option == "4":
        run_query(query18)
        run_query(query19)
        run_query(query20)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    select_query()


