time = int(input("Введите время в секундах: "))


hours = int(time/3600)
minutes = int((time - hours * 3600) / 60)
seconds = int(time - hours * 3600 - minutes * 60)

print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")
