from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el year %Y')
print(f'Formato Random: {my_str}')

my_str = my_datetime.strftime('%H:%M')
print(f'Formato de 24 hs: {my_str}')

my_str = my_datetime.strftime('%I:%M')
print(f'Formato de 12hs: {my_str}')

my_str = my_datetime.utcnow()
print(f'Formato UTC now: {my_str}')
