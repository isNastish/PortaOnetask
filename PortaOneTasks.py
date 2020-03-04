file = open('originalFile.txt').readlines() # Чмтаем файл.
list1 = [int(i.rstrip()) for i in file] # Создем список всех целых чисел в файле.

LengthGrow = [] # Здесь будет сохраняться число(длинна наибольшой возрастающей последовательности).
LengthFall = [] # Аналогично LengthGrow только(длинна наибольшой убывающей последовательности).
# Находим медиану чисел в исходном файле.
for j in range(len(list1)):
    if (len(list1) % 2) != 0: # Если количество чисел не четное.
        if j == ((len(list1) - 1) / 2): # Отнимем 1 и делим на 2, потому что это как раз индекс числа середины.
            print('Median: %i' % (list1[j]))
            break # Если нашли - сразу выходим из этого цикла.
    else:
        if j == (len(list1) // 2): # Следующее число после среднего.
            print('Median: %.4f' % ((list1[j] + list1[j - 1]) / 2))
            break
# Наибольшая возрастающая последовательность.
for k in range(len(list1)):
    if not k:
        Grow = []
        Grow.append(list1[k])
        countGrow = 1
    elif k:
        if (list1[k] > list1[k - 1]):
            Grow.append(list1[k])
            countGrow += 1
            if k == (len(list1) - 1) and countGrow > LengthGrow[0]: # На случай если последнее число сформирут самую большую последовательность.
                LengthGrow[0] = countGrow
                tempGrow = [] # Для  хранения самой большой (ОДНОЙ) последовательности.
                tempGrow += Grow
        else:
            if not LengthGrow:LengthGrow.append(countGrow)
            if (countGrow > LengthGrow[0]): # Если длинна последовательности больше чем предыдущей.
                LengthGrow[0] = countGrow # Заносим число (длинна последовательности сформированнной до последнего обрывания).
                tempGrow = [] # Если длинна последовательности окажиться больше чем предыдущая, мы чистим tempGrow.
                # и добавляем всю последовательность с Grow в tempGrow
                tempGrow += Grow
            Grow = [] # При появлении числа которое ламает последовательность список очиститься!
            Grow.append(list1[k]) # Добавляем первое значение новой последовательности.
            countGrow = 1
# Наибольшая убывающая последовательность.
for k in range(len(list1)):
    if not k:
        Fall = []
        Fall.append(list1[k])
        countFall = 1
    elif k:
        if (list1[k] < list1[k - 1]):
            Fall.append(list1[k])
            countFall += 1
            if k == (len(list1) - 1) and countFall > LengthFall[0]:
                LengthFall[0] = countFall
                tempFall = []
                tempFall += Fall
        else:
            if not LengthFall:LengthFall.append(countFall)
            if (countFall > LengthFall[0]):
                LengthFall[0] = countFall
                tempFall = []
                tempFall += Fall
            Fall = []
            Fall.append(list1[k])
            countFall = 1
print('Biggest Decrease list:',tempFall,\
    'Length:',len(tempFall),'\n'\
    'Biggest Increase list:',tempGrow,\
    'Length:',len(tempGrow),'\n'\
    'Maximum:',max(list1),'\n'\
    'Minimum:',min(list1))

