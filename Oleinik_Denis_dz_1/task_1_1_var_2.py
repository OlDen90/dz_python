duration = int(input('Введите  число: '))

sec_in_min = 60
sec_in_hour = 3600
sec_in_day = 86400
sum_of_sek = sec_in_hour - duration
sum_of_hours = sec_in_day - duration

sum_of_min = sum_of_hours - ((sum_of_hours // sec_in_hour) * sec_in_hour)

seconds = sum_of_sek % 60
minutes = sum_of_sek // 60
hours = sum_of_hours // 3600

if duration < sec_in_min:
    print('duration =', duration)
    print('До минуты осталось', sec_in_min - duration, 'сек')
elif duration >= sec_in_min and duration < sec_in_hour:
    print('duration =', duration)
    print('До часа осталось', minutes, 'мин', seconds, 'сек')
elif duration >= sec_in_hour and duration < sec_in_day:
    print('duration =', duration)
    print('До суток осталось', hours, 'час(ов)', sum_of_min // sec_in_min, 'мин', seconds, 'сек')
else:
    print('Таймер работает в диапозоне до 24-х часов. Пожалуйста, введите новое число.')