duration = int(input('Введите промежуток времени в секундах: '))
seconds = duration

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

if duration < 60:
    result = f'{duration} сек'
elif duration < 3600:
    result = f'{minutes} мин {seconds} сек'
elif duration < 86400:
    result = f'{hours} час {minutes} мин {seconds} сек'
else:
    result = f'{days} дн {hours} час {minutes} мин {seconds} сек'

print(result)
