'''
Задача: дан список температур, которые считал датчик.
Датчик считывает температуру каждую секунду.
Если одна из температур больше/равна 34 и меньше/равна 40
то поднять тревогу (какое-то существо проникло на базу)
иначе сообщить, что проблем нет.
'''

spisokT = [1, -45, 31, 20, 36.6, 100, 80, 54.6]

trevoga = False

for t in spisokT:
    if t >= 34 and t <= 40:
        trevoga = True
        break

if trevoga == True:
    print("Тревога! Посторонний на территории")
else:
    print("Угроз не обнаружено")
