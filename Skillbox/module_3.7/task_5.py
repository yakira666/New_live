data_time = int(input("Введите число в минутах: "))
hour = data_time // 60
final_minutes = data_time % 60

print(f'{hour} часов {final_minutes} минут')
