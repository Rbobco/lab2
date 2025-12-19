from collections import Counter


def input_array():
    while True:
        try:
            input_str = input()
            array = [int(x) for x in input_str.strip().split()]
            if not array:
                print("Массив не может быть пустым")
                continue
            return array
        except ValueError:
            print("Ошибка: Введите только целые числа через пробел")


def find_repeating_in_b(A, B):
    b_count = Counter(B)
    result = set()
    for i in A:
        if b_count[i] > 1:
            result.add(i)
    if result != set():
        return sorted(list(result))
    else:
        return ("Таких элементов нет")


def find_unique_in_a_multiple_in_b(A, B):
    a_count = Counter(A)
    b_count = Counter(B)
    result = set()
    for i in A:
        if a_count[i] == 1 and b_count[i] > 1:
            result.add(i)
    if result != set():
        return sorted(list(result))
    else:
        return ("Таких элементов нет")


def find_multiple_in_both(A, B):
    a_count = Counter(A)
    b_count = Counter(B)
    result = set()
    for i in a_count:
        if a_count[i] > 1 and b_count.get(i, 0) > 1:
            result.add(i)
    if result != set():
        return sorted(list(result))
    else:
        return ("Таких элементов нет")


def main():
    A = []
    B = []
    print("Программа для работы с массивами A и B")
    print("Меню:")
    print("1. Ввод массивов")
    print("2. Элементы А, повторяющиеся в В несколько раз")
    print("3. Неповторяющиеся, элементы А,"
          "которые присутсвуют в В в нескольких экземплярах")
    print("4. Элементы, присутсвующие в обоих массивах "
          "в нескольких экземплярах")
    print("5. Показать меню снова")
    print("0. Выход")
    while True:
        choice = input("Выберете вариант(цифра): ")

        if choice == "1":
            print("Программа принимает элементы массива через пробел."
                  "Пример - 1 2 3")
            print("Введите массивы A и B по очереди")
            A = input_array()
            B = input_array()
        elif (choice in ["2", "3", "4"] and (A == [] or B == [])):
            print("Сначала введите элементы массива")
        elif choice == "2":
            result = find_repeating_in_b(A, B)
            print("Результат:", result)
        elif choice == "3":
            result = find_unique_in_a_multiple_in_b(A, B)
            print("Результат:", result)
        elif choice == "4":
            result = find_multiple_in_both(A, B)
            print("Результат:", result)
        elif choice == "5":
            print("Меню:")
            print("1. Ввод массивов")
            print("2. Элементы А, повторяющиеся в В несколько раз")
            print("3. Неповторяющиеся, элементы А,"
                  "которые присутсвуют в В в нескольких экземплярах")
            print("4. Элементы, присутсвующие в обоих массивах "
                  "в нескольких экземплярах")
            print("5. Показать меню снова")
            print("0. Выход")
        elif choice == "0":
            break
        else:
            print("Такой функции нет в меню")


main()
