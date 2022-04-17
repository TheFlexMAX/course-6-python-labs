import requests

city = "Odessa,UA"
appid = "85d1a7314de3ff7329f385dbdfb3c27f"


def weekly_weather():
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print("Прогноз погоды на неделю:")
    for i in data['list']:
        print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
              "> \r\nПогодные условия <", i['weather'][0]['description'], ">", f"\r\nВидимость <{i['visibility']}>",
              f"\r\nСкорость ветра < {i['wind']['speed']} >")

        print("____________________________")


def today_weather():
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    print("Город:", city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Видимость", data['visibility'])
    print("Скорость ветра", data['wind']['speed'])


def main():
    # today_weather()
    weekly_weather()


if __name__ == '__main__':
    main()
