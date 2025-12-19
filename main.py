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
    from collections import Counter
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
    from collections import Counter
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

print(find_unique_in_a_multiple_in_b(input_array(), input_array()))