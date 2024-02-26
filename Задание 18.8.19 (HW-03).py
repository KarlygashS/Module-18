ticket_sum = 0
ticket_quantity = int(input("Введите необходимое количество билетов: "))
for age in range(ticket_quantity):
    age = int(input("Введите возраст каждого посетителя: "))
    if age < 18:
        ticket_sum += 0
    elif 18 <= age < 25:
        ticket_sum += 990
    elif age >= 25:
        ticket_sum += 1390
    print("Итого к оплате: ", ticket_sum)
if ticket_quantity >= 3:
    ticket_sum_discounted = ticket_sum - (ticket_sum * 10 / 100)
    print("Итого к оплате с учетом скидки: ", ticket_sum_discounted)
