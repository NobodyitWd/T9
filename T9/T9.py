first = input("input any word:    ")
inpath = input(r"Input path:    ")
# Если имеется массив по пути не обязательно вводить его каждый раз. Закоментируй inpath и создай: inpath = r"путь\путь\путь\массив"
def Readerwords(inpath):
    i = 0
    ii = 1
    first = 0
    second = 1
    last = [0] # 0 - Точка отсчета. Исключает ошибку с неверным индексом.
    mass = []

    file = open(inpath,"r",encoding="UTF-8") # откроем файл.
    fileread = (file.read()) # Содержимое.

    while i != len(fileread): # Пока i не равно количеству символов содержимого.
        if fileread[i] == " ": # Если находим пробел.
            last.append(i+1) # Добавляем его айди в список.
        if fileread[i] == "\n": # Если находим переход строки.
            last.append(i+1) # Добавляем его айди в список.
        i += 1
    last.append(len(fileread)) # Добавляем кол символов в список с индексом пробелов. Исключает ошибку с неверным индексом.
    while ii != len(last): # Пока ii не равно кол индексов пробела.
        mass.append(fileread[last[first]:(last[second]-1)]) # Добавить в список mass символы от first до second-1. -1 для исключения последнего символа. Им являеться пробел.
        first += 1
        second += 1
        ii += 1
    return mass
def T9(first,second):
    mass = [] # Массив с максимальным числом. т.е.с - таблица.
    used = [] # Массив с использованными числами. исключает повторения.
    used1 = [] # Массив с использованными числами №2. исключает повторения, однако конфликтует с первым массивом использованных чисел.
    i = 0
    j = 0
    subsequence = 0 # Текущее максимальное число
    while len(first) != i and len(second) != j: # Пока кол. букв в введенном слове не равно числу повторений i, и пока кол. букв в слове из массива слов не равно числу повторений j.
        if first[i] == second[j] and first[i] not in used and second[j] not in used and first[j] not in used and second[i] not in used: # Если буква i == букве j, и она не была использована раннее. Если перевести в табличный вид - буква i ось x, буква j - ось y.
            subsequence += 1 # Текущее макс. число + 1.
            mass.append(subsequence) # Добавить текущее макс. число.
            used.append(first[i]) # Добавить текущее макс. число в список использованных.
        if first[i] != second[j] and first[i]+second[j] not in used1: # Если буква i не равна букве j, и буква i + j не в списке использованных.
            mass.append(subsequence) # Добавить текущее максимальное число.
            used1.append(first[i]+second[j]) # Добавить букву i + j в список использованных. (Если добавить только i или j то остальные буквы начинающиеся на i или j будут пропущенны).
        if first[j] == second[i] and second[i] not in used and first[j] not in used and first[i] not in used and second[j] not in used: # ----------------
            mass.append(subsequence)
            used.append(first[i]) # Здесь все тоже самое за исключением замены i на j и j на i. ((Нужно для проверки по оси y.)Раньше проверяли таблицу с лева на право. Сейчас с верху в низ).
        if first[j] != second[i] and first[j]+second[i] not in used1: # Обьеденив данные и (уже) искличив повторения мы получим таблицу с максимальной последовательностью букв.
            mass.append(subsequence)
            used1.append(first[j]+second[i]) # ------------------------------------------------------------------------------------------------------------
        j += 1
        if len(second) == j or len(first) == j: # Дабы цикл не закончился раньше времени.
            i += 1 # Мы добавляем i + 1 когда строка j или i проверенна полностью.
            j = i # И j теперь начинается с i, чтобы не заполнять оси i таблицу j или наоборот.
    return max(mass)
used = []
id = []
mass = Readerwords(inpath) # Загружаем массив слов.
i = 0
j = 0
k = 0
while i != len(mass):
    second = (mass)[i]
    used.append(T9(first, second)) # Обрабатываем с помощью Т9 наш массив данных. Получаем значение каждого слова в массиве по отношению к введенному слову.
    i+=1
maximum = max(used)
while j != len(used): # Просматриваем полученный значения и находим максимальные.
    if used[j] == maximum: # Если j будет максимальное число.
        id.append(j) # Добавь j в id.
    j += 1
print("Возможно вы имели в виду:    ")
while k != len(id): # Если нужно ограничить кол. возможных слов - добавь в этот цикл условие:   and k != (число слов) - 1
    print(mass[id[k]]) # Покажи слова с максимальным значением для введенного слова.
    k+=1