staff = ['инженер-конструктор игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for person in staff:
    name = person.split(' ')[-1].title()
    print('Привет,', name + '!')

# person_1 = staff[0].title()
# name_1 = person_1.split(' ')
# print('Привет', name_1[-1] + '!')
#
# person_2 = staff[1].title()
# name_2 = person_2.split(' ')
# print('Привет', name_2[-1] + '!')
#
# person_3 = staff[2].title()
# name_3 = person_3.split(' ')
# print('Привет', name_3[-1] + '!')
#
# person_4 = staff[3].title()
# name_4 = person_4.split(' ')
# print('Привет', name_4[-1] + '!')
