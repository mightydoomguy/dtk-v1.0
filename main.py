
#----------------------------------------
import webbrowser as wb
import math as m
import cowsay
from colorama import Fore,Back,Style
import requests
from data import *
#----------------------------------------
num=132
while num != 0:
    cowsay.cow(Fore.RED + "Daily.ToolKit.v1 by mightydoomguy")
    print(Style.BRIGHT + Fore.CYAN + "#--------Main_menu-------\n"
          + Fore.MAGENTA + "1.Математические функции\n2.Соц.сети\n3.Прогноз погоды\n4.Справка\n0.Выход\n",
          Fore.CYAN + "#------------------------")

    num = int(input("Выбери пункт:>>>"))
#-------------------------------------------------------------------------------
    if num == 1:
        print( Fore.MAGENTA + "1.Калькулятор\n"
              "2.Тригонометричесие функции\n")
        n = int(input(Fore.CYAN +"Выбери пункт:>>>"))
        e = 0
        if n == 1:
            q = int(input("Выбери операцию:1.Сложение 2.Вычитание 3.Умножение 4.Умножение\n"))
            if q == 1:
                x = int(input("Введи первое число:"))
                y = int(input("Введи второе число:"))
                print(Fore.YELLOW + "Результат сложения:", x + y)
            elif q == 2:
                x = int(input("Введи первое число:"))
                y = int(input("Введи второе число:"))
                print(Fore.YELLOW +"Результат вычитания:", x - y)
            elif q == 3:
                x = int(input("Введи первое число:"))
                y = int(input("Введи второе число:"))
                print(Fore.YELLOW +"Результат умножения:", x * y)
            elif q == 4:
                x = int(input("Введи первое число:"))
                y = int(input("Введи второе число:"))
                print(Fore.YELLOW +"Результат деления:", x / y)
#--------------------------------------------------------------------------------
        elif n == 2:
            w = int(
                input("1.Нахождение синуса \n 2.Нахождение косинуса\n 3.Нахождение тангенса\n 4.Нахождение котангенса\n Выбери пункт:>>>"))
            if w == 1:
                num1 = int(input("Enter num:"))
                print("Синус твоего числа", round(m.sin(num1)))
            elif w == 2:
                num1 = int(input("Enter num:"))
                print("косинус твоего числа", round(m.cos(num1)))
            elif w == 3:
                num1 = int(input("Enter num:"))
                print("Тангенс твоего числа", round(m.tan(num1)))
            elif w == 4:
                num1 = int(input("Enter num:"))
                print("Котангенс твоего числа", round(m.sin(num1)))
            elif w == 0:
                continue
        elif n==3:
            num2 = float(input("Enter num:"))
            res = m.log10(num2)
            print("Логарифм твоего числа:")
            print(res)
# --------------------------------------------------------------------------------
    elif num == 2:
        print("1.Vk\n"
              "2.ok\n"
              "3.facebook\n"
              "4.Википедия")
        sw = int(input("Enter social network:>>>"))
        if sw == 1:
            wb.open_new_tab("https://vk.com")
        elif sw == 2:
            wb.open_new_tab("https://ok.ru")
        elif sw == 3:
            wb.open_new_tab("https://facebook.com")
        elif sw == 4:
            wb.open_new_tab('https://ru.wikipedia.org/wiki/')
        elif sw == 0:
            continue
# --------------------------------------------------------------------------------
    elif num==3:
        print(Fore.WHITE + "Cписок доступных городов:\n"
              "Мегион\n",
     "Санкт-Петербург\n",
     'Москва\n',
     "Сургут\n",
     "Уфа\n",
     "Волгоград\n",
     "Краснодар\n",
     "Ханты-Мансийск\n",
     "Когалым\n",
     "Лянтор")
        s_city = input(Fore.BLUE+ "Enter city:>>>")
        print(Fore.RED + "Погода в городе:" + Fore.BLUE+ s_city + "\n")
        city_id = d.get(s_city)
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast/",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print('  Дата и время ' + "   Градусы " + "  Осадки")
            for i in data['list']:
                print(Fore.YELLOW + i['dt_txt'], Fore.RED + '{0:+3.0f}'.format(i['main']['temp']), Fore.MAGENTA + i['weather'][0]['description'])
        except Exception as e:
            print("Exception (forecast):", e)
            pass
#----------------------------------------------------------------------------------
    elif num==4:
        print(Fore.YELLOW + "Эта программа создана с целью упрощения повседневных дел у студентов и знайте что кроме студентов\n ее нежелательно использовать другим сущностям"
                            "и если вам что-то не нравится в моей программе взяли и принялись исправлять и добавлять свои фичи делал я ее для себя и мне это в кайф\n "
                            "И так в функционал программы входит:Математические функции где можно будет использовать калькулятор и тригонометрические функции(Будет дорабатываться).\n"
                            " Соц.сети где можно будет посетить ссылки на те соц сети которые имеются здэсь \n"
                            "Прогноз погоды где можно узнать о погоде введеного вами города(Есть конфиг файл data.py там добавляете свои города и их id используется сервис openweathermap а также API-ключ который находится в профиле так что нужно зарегаться на owm)\n")