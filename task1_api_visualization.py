import requests
import matplotlib.pyplot as plt
import seaborn as sns
import sys

API_KEY = "c882d501810db5eb3b3b3dcc3ae01221"
CITY = "Pune,IN"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Check API response
if "list" not in data:
    print("API Error:", data)
    sys.exit()

dates = []
temperatures = []
humidity = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])
    humidity.append(item["main"]["humidity"])

plt.figure(figsize=(12, 6))

# Temperature subplot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temperatures)
plt.xticks(rotation=45)
plt.title("Temperature Forecast for Pune")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")

# Humidity subplot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidity)
plt.xticks(rotation=45)
plt.title("Humidity Forecast for Pune")
plt.xlabel("Date and Time")
plt.ylabel("Humidity (%)")

plt.tight_layout()
plt.show()

