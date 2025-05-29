import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

URL = "https://www.timeanddate.com/weather/latvia/riga"

def get_weather():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Neizdevās piekļūt laikapstākļu vietnei.")

    soup = BeautifulSoup(response.content, "html.parser")

    temp_element = soup.find("div", class_="h2")
    condition_element = soup.find("p")
    extra_info = soup.find_all("tr")

    weather_data = {
        "temperatūra (°C)": temp_element.text.strip().replace("°C", "").strip() if temp_element else "N/A",
        "apraksts": condition_element.text.strip() if condition_element else "N/A",
        "vēja ātrums": "N/A",
        "mitrums": "N/A",
        "datums": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    for row in extra_info:
        cols = row.find_all("td")
        if len(cols) >= 2:
            key = cols[0].text.strip().lower()
            value = cols[1].text.strip()
            if "wind" in key or "vējš" in key:
                weather_data["vēja ātrums"] = value
            elif "humidity" in key or "mitrums" in key:
                weather_data["mitrums"] = value

    return weather_data

def save_to_csv(data, filename="weather_log.csv"):
    lauki = list(data.keys())
    try:
        with open(filename, "x", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=lauki)
            writer.writeheader()
            writer.writerow(data)
    except FileExistsError:
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=lauki)
            writer.writerow(data)

def main():
    try:
        weather = get_weather()
        save_to_csv(weather)
        print("Laikapstākļu dati veiksmīgi saglabāti!")
    except Exception as e:
        print(f"Kļūda: {e}")

if __name__ == "__main__":
    main()
