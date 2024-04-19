import requests
from bs4 import BeautifulSoup


def check_weather(city):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }

    responce = requests.get(
        f"https://www.google.com/search?q=погода+в+{city}", headers=headers)
    print(responce)

    soup = BeautifulSoup(responce.text, "html.parser")

    temperature = soup.select("#wob_tm")[0].getText()
    title = soup.select("#wob_dc")[0].getText()
    humidity = soup.select("#wob_hm")[0].getText()
    time = soup.select("#wob_dts")[0].getText()
    wind = soup.select("#wob_ws")[0].getText()

    def time_hour(time):
        return f'{time[:-3]} утра' if int(time[-5:-3]) <= 12 else f'{time[:-5]}{int(time[-5:-3])-12} вечера'

    print(time_hour(time))
    print(title)
    print(f"Температура: {temperature}C")
    print(f"Влажность: {humidity}")
    print(f"Ветер: {wind}")


if __name__ == "__main__":
    city = str(input("Город: "))
    check_weather(city=city)
