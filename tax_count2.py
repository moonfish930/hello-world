def tax_common(salary):
    tax = 0
    if salary <= 36000: tax = salary*0.03
    elif 36000<salary<=144000:  tax = salary*0.1-2520
    elif 144000<salary<=300000: tax = salary*0.2-16920
    elif 300000<salary<=420000: tax = salary*0.25-31920
    elif 420000<salary<=660000: tax = salary*0.3-52920
    elif 660000<salary<=960000: tax = salary*0.35-85920
    else:   tax = salary*0.45-181920
    return tax

def tax_bonus(bonus):
    salary = bonus//12
    tax = 0
    if salary<=3000: tax = bonus*0.03
    elif 3000<salary<=12000: tax = bonus*0.1 - 210
    elif 12000<salary<=25000: tax = bonus*0.2 - 1410
    elif 25000<salary<=35000: tax = bonus*0.25 - 2660
    elif 35000<salary<=55000: tax = bonus*0.3 - 4410
    elif 55000<salary<=80000: tax = bonus*0.35 - 7160
    else: tax = bonus*0.45 - 15160
    return tax


def distri(salary):
    common = 0
    bonus = salary - common
    max_bonus = bonus
    min_tax = salary
    for i in range(salary):
        common,bonus = i,salary - i
        tmp = tax_common(common) + tax_bonus(bonus)
        if int(tmp) < int(min_tax):
            max_bonus = bonus
            min_tax = tmp

    bonus,min_bonus = max_bonus,max_bonus
    while 1:
        bonus -=1
        common = salary - bonus
        tmp = tax_common(common) + tax_bonus(bonus)
        if int(tmp) > int(min_tax):
            bonus +=1
            min_bonus = bonus
            break
    if min_bonus < 0: min_bonus = 0

    return (min_bonus,max_bonus,min_tax)

while True:
    salary = int(input("Salary: "))   
    print(distri(salary))
