# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монеток > '))
count_orel = 0
count_reshka = 0

print('Поочередно введите как лежат монеты. 0 - орел, 1 - решка.')
for i in range(n):
    x = int(input(f'Монета {i+1} из {n} >'))
    if x == 0:
        count_orel +=1
    else:
        count_reshka +=1
if count_orel > count_reshka:
    print(f'Нужно перевернуть {count_reshka} штук')
else:
    print(f'Нужно перевернуть {count_orel} штук')