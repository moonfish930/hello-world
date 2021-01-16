def all(month, bonus):
    new_month = 0
    min_month, min_bonus = month, bonus
    new_bonus = 12*month +bonus
    total = 12*month +bonus
    min_tax = month*12+bonus
    for i in range(0,total,12):
        new_bonus -=12
        new_month +=1
        tmp = count_month(new_month)*12 + count_bonus(new_bonus)
        if tmp<min_tax:
            min_month = new_month
            min_bonus = new_bonus
            min_tax = tmp
    return (min_month,min_bonus,min_tax)

def count_month(salary):
    tax = 0
    if salary<=3000: tax = 0
    elif 3000<salary<=12000: tax = salary*0.1 - 210
    elif 12000<salary<=25000: tax = salary*0.2 - 1410
    elif 25000<salary<=35000: tax = salary*0.25 - 2660
    elif 35000<salary<=55000: tax = salary*0.3 - 4410
    elif 55000<salary<=80000: tax = salary*0.35 - 7160
    else: tax = salary*0.45 - 15160
    return tax

def count_bonus(bonus):
    salary = bonus//12
    tax = 0
    if salary<=3000: tax = 0
    elif 3000<salary<=12000: tax = bonus*0.1 - 210
    elif 12000<salary<=25000: tax = bonus*0.2 - 1410
    elif 25000<salary<=35000: tax = bonus*0.25 - 2660
    elif 35000<salary<=55000: tax = bonus*0.3 - 4410
    elif 55000<salary<=80000: tax = bonus*0.35 - 7160
    else: tax = bonus*0.45 - 15160
    return tax


month = int(input("Month: "))
bonus = int(input("Bonus: "))

(min_month, min_bonus, min_tax) = all(month,bonus)
print((min_month, min_bonus, min_tax))