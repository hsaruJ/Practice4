import datetime

year, month, day = [int() for i in range(3)]
try:
    year, month, day = map(int, input("Введите дату рождения в формате YYYY/MM/DD\n").split("/"))
except ValueError:
    print("Ошибка: не соблюдён формат ввода. Перезапустите, чтобы продолжить.")
    exit()


day_of_birth = int()
try:
    day_of_birth = datetime.datetime(year, month, day, hour=12)
except ValueError:
    print("Ошибка: несуществующая дата. Перезапустите, чтобы продолжить.")
    exit()

print("Будем считать, что вы родились в 12:00.")
day_10_000_days = day_of_birth + datetime.timedelta(days=10_000)
print("День, в который Вам исполнится 10'000 дней:", day_10_000_days.date())

day_million_minutes = day_of_birth + datetime.timedelta(minutes=1_000_000)
print("День, когда вам исполнится 1'000'000 минут:", day_million_minutes.date())

day_billion_seconds = day_of_birth + datetime.timedelta(seconds=1_000_000_000)
print("День, когда Вам исполнится 1'000'000'000 секунд:", day_billion_seconds.date())
