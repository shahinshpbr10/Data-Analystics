import requests as r
import json
from secret import key

city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = r.get(url)
print("Status code:", response.status_code)

if response.status_code == 200:
    # Convert JSON response to formatted text
    data = response.json()
    text_output = json.dumps(data, indent=2)

    # Print the formatted text output
    print("Response JSON:")
    print(text_output)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
