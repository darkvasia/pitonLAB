# Калкулятор 

print ('Вітаю в калкуляторі  Python')
q1 = int (input('Ввести число 1: '))
q2 = int (input('Ввести число 2: '))

v = int (input('Яку операцію ви хочете виконати? \n 1 Додавання \n 2 Віднімання \n 3 Ділення \n 4 Множення \n'))

if v == 1:
    r = q1 + q2
    p = 'Додавання'
    t = p
if v == 2:
    r = q1 - q2
    l = 'Віднімання'
    t = l
if v == 3:
    r = float(q1 / q2)
    m = 'Ділення'
    t = m
if v == 4:
    r = q1 * q2
    n = 'Множення'
    t = n
print ('Результат ',t,' = ',r)