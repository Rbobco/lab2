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
            