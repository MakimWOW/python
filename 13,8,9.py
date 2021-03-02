count = int(input("Введите количество билетов:"))
s = 0
for price in range(1, count + 1):
    age = int(input("Введите возраст участников:"))
    if 0<= age <= 18:
        price = 0
    elif 18 <= age <= 25:
        price = 990
    elif 25 <= age <= 99:
         price = 1390
    else: print("Невереный возраст")
if count > 3:
    s = (s + ((price * count)*0.9))
    print("Общая стоимость билетов:",s)
else:
    s = (s + (price * count))
    print("Общая стоимость билетов:",s)
print("Цена билетов = ",s)
