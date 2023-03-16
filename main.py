from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
#print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = dt.datetime.now()
date_in_six_months = today + dt.timedelta(days=180)

LOCAL_AIRPORT = "SFO"

for destination in sheet_data:
    flight = flight_search.check_flights(
        LOCAL_AIRPORT,
        destination["iataCode"],
        from_time=today,
        to_time=date_in_six_months
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )
