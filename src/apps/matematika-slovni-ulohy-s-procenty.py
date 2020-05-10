# Credits
#   - Monika Sistkova: Initial version - interactive in terminal
#   - Vaclav Sistek: Modification for cgi and json output


import random
import json

pocitac = random.randint(1,4)
zbozi = ("Kabelka", "Jízdenka", "Bunda", "Vstupenka na koncert", "Hračka", "Kniha","Vstupenka do divadla")
zbozi = random.choice(zbozi)
if pocitac == 1:
    sc = 0.5
    while not sc % 1 == 0:
        procent = random.randint(2,9) * 5
        pc = random.randint(10,90) * 10
        sc = (100-procent)/100 * pc
    task = '{} stála před Vánoci {} Kč a byla zlevněna o {} %. Kolik stojí nyní?'.format(zbozi,pc,procent)
    solution = sc
elif pocitac == 2:
    pc = 0.5
    while not pc % 1 == 0:
        procent = random.randint(2,9) * 5
        sc2 = random.randint(25,150)* 10
        pc = 100/(100-procent) * sc2
    task = '{} byla zlevněna o {} '%' a nyní stojí {} Kč. Jaká byla původní cena?'.format(zbozi,procent,sc2)
    solution = pc
elif pocitac == 3:
    x = 0.5
    while not x % 1 == 0:
        procent = random.randint(2,9) * 5
        okolik = random.randint(10,40) * 10
        x = (100+procent)/procent * okolik
    task = '{} byla zdražena o {} Kč, což je {} %  ceny. Kolik stojí nyní?'.format(zbozi,okolik,procent)
    solution = x
elif pocitac == 4:
    y = 0.5
    while not y % 1 == 0:
        procent = random.randint(2,9) * 5
        sc3 = random.randint(25,150)* 10
        y = 100/(procent+100) * sc3
    task = '{} byla zdražena o {} %  a nyní stojí {} Kč. Jaká byla původní cena?'.format(zbozi,procent,sc3)
    solution = y

print(json.dumps([task, "{0:d} Kč".format(int(solution))]))
