duration = int(input('Введите  число: '))

sec_in_min = 60
sec_in_hour = 3600
sec_in_day = 86400

count_sec = duration % 60
count_min = duration % 3600
count_hours = duration % 86400

minutes = count_min // 60
hours = count_hours // 3600

if duration < sec_in_min:
    print('duration =', duration)
    print(duration, 'сек')
elif duration >= sec_in_min and duration < sec_in_hour:
    print('duration =', duration)
    print(duration // sec_in_min, 'мин', count_sec, 'сек')
elif duration >= sec_in_hour and duration < sec_in_day:
    print('duration =', duration)
    print(duration // sec_in_hour, 'час(а/ов)', minutes, 'мин', count_sec, 'сек')
else:
    print('duration =', duration)
    print(duration // sec_in_day, 'день(дней)', hours, 'час(а/ов)', minutes, 'мин', count_sec, 'сек')