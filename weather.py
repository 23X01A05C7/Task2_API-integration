import requests

city = input("Enter city: ")

url = f"https://wttr.in/{city}?format=j1"

try:

    response = requests.get(url)

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]

    weather = data["current_condition"][0]["weatherDesc"][0]["value"]

    humidity = data["current_condition"][0]["humidity"]

    print("\n------ WEATHER REPORT ------")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Weather Condition:", weather)
    print("Humidity:", humidity, "%")

except Exception as e:

    print("Error:", e)