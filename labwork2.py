import requests

city = input("Введите название города\n(например, \"London,GB\"):\n")
#city = "Mayami,US"
appid = "89d594d3595e30e2df633b1767f11939"

res=requests.get("http://api.openweathermap.org/data/2.5/weather",params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print("Город:",city)
print("\nПогода сейчас\nПогодные условия:",data['weather'][0]['description'])
print("Температура:",data['main']['temp'])
print("Минимальная температура:",data['main']['temp_min'])
print("Максимальная температура:",data['main']['temp_max'])
print("Скорость ветра (м/с):",data['wind']['speed'])
print("Видимость (м):",data['visibility'])

res=requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()
print("\n\nПрогноз погоды на неделю:")
for i in data['list']:
    print("Дата <",i['dt_txt'],"> \r\nТемпература <",'{0:+3.0f}'.format(i['main']['temp']),"> \r\nПогодные условия <",i['weather'][0]['description'],\
        "> \r\nСкорость ветра <",i['wind']['speed'],"м/с > \r\nВидимость <",i['visibility'],"м >\n")
print("____________________________\n")
