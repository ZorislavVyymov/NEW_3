"""
Задание:
Пользователь вводит количество элементов будущего списка.
После этого по очереди по одной вводит любые цифры.
Сохранить цифры в список.
Отсортировать список по возрастанию и вывести на экран
"""
count = 0
my_list = []
n = int(input('Задайте количество элементов списка (любым целым числом): '))
while count < n:
    count +=1
    my_list.append(int(input('Введите '+str(count)+' элемент списка: ')))
    print(my_list)
print("Отсортированный по возрастанию список:")
my_list.sort()  # Сортируем список
print(my_list)  # Выводим отсортированный список